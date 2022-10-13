import re
from datetime import date, datetime
from string import ascii_letters
from time import sleep
from typing import Dict, List, Set
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.sessions import Session
from tenacity import retry, wait_exponential
from urllib3.util import Retry

from cisei.cisei_database import Database
from data_types.person_info import PersonInfo


class CiseiRequestHandler:
    URL: str = "http://www.ciseionline.it/portomondo/ricerca.asp"
    BASE_PERSON_URL: str = "http://www.ciseionline.it/portomondo/"
    NEXT_PAGE_URL: str = "http://www.ciseionline.it/portomondo/tabelle.asp?primo="
    MAX_RESULTS_PER_PAGE: int = 16
    DELAY: float = 0.05

    def __init__(self) -> None:
        self.db = Database()
        self.session = self._init_session()

    def _init_session(self) -> Session:
        session = Session()
        retries = Retry(connect=10, read=10, redirect=10)

        session.mount("http://", HTTPAdapter(max_retries=retries))
        session.mount("https://", HTTPAdapter(max_retries=retries))
        session.headers.update(
            {
                "User-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
            }
        )
        return session

    @retry(wait=wait_exponential(multiplier=1, min=2, max=5))
    def get_first_page(self, surname: str) -> BeautifulSoup:
        custom_header = {
            "input_cognome": surname,
            "input_nome": "",
            "input_dest": "al",
        }
        req = self.session.post(self.URL, custom_header)
        req.raise_for_status()
        content = req.content
        soup = BeautifulSoup(content, "html.parser")
        return soup

    @retry(wait=wait_exponential(multiplier=1, min=2, max=5))
    def get_next_page(self, page: int) -> BeautifulSoup:
        cookie = self.session.cookies.get_dict()
        cookie_list = list(cookie.items())[0]
        cookie_str = f"{cookie_list[0]}={cookie_list[1]}"
        custom_header = {
            "Cookie": cookie_str,
            "Connection": "keep-alive",
        }
        url = self.NEXT_PAGE_URL + str(page)
        req = self.session.get(url, headers=custom_header)
        req.raise_for_status()
        content = req.content
        soup = BeautifulSoup(content, "html.parser")
        return soup

    @retry(wait=wait_exponential(multiplier=1, min=2, max=5))
    def get_details_soup(self, details_url: str) -> BeautifulSoup:
        r = self.session.get(details_url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")
        return soup

    @staticmethod
    def remove_alphanumeric(arg: str) -> str:
        return "".join([c for c in arg if c in (ascii_letters)])

    def get_person_info(self, td_list: List, name: str) -> PersonInfo:
        idx: str = td_list[0].text

        age: List[str] = re.search(r"\d+", td_list[2].text)
        age: str = age.group(0) if age is not None else None

        full_name_reg_res: List[str] = re.findall(r"[A-Z]+", td_list[1].text)
        full_name: str = (
            " ".join(full_name_reg_res).replace(name.upper() + " ", "").title()
            if full_name_reg_res is not None
            else ""
        )

        trip_date_reg_res: List[str] = re.findall(r"\d{1,4}", td_list[3].text)
        trip_date: date = (
            datetime.strptime("-".join(trip_date_reg_res), "%d-%m-%Y")
            if len(trip_date_reg_res) != 0
            else None
        )

        registration_place_reg_res: List[str] = re.findall(
            r"\b[A-Z\w+]+", td_list[4].text
        )
        registration_place: str = (
            " ".join(registration_place_reg_res)
            if registration_place_reg_res is not None
            else ""
        )

        details: str = str(td_list[5].contents[1]).split('"')[1]

        person_info: PersonInfo = PersonInfo(
            idx=idx,
            surname=name,
            full_name=full_name,
            age=age,
            trip_date=trip_date,
            registration_place=registration_place,
            url=urljoin(self.BASE_PERSON_URL, details),
        )

        return person_info

    def get_person_details(self, person: PersonInfo) -> Dict:
        soup: BeautifulSoup = self.get_details_soup(person.url)
        td_list: List = soup.find_all("td")
        details_dict: Dict = {}
        for tr in td_list:
            raw_txt: List[str] = re.sub(r"\\<[/]?[a-z]\\>", "", tr.text).splitlines()

            for line in raw_txt:
                try:
                    k, v = line.split(":")
                    key = k.strip()
                    value = v.strip()
                    if value not in ["", "nd", "ND", "n.d.", "N.D."]:
                        details_dict[key] = value
                except ValueError:
                    pass

        return details_dict

    def parse_page(self, name: str, soup: BeautifulSoup) -> None:
        try:
            tr_list: List = (
                soup.find("div", {"class": "box"}).find("center").find_all("tr")
            )
        except AttributeError:
            print(f"No results for {name}")
            return
        for tr in tr_list:
            td_list: List[str] = tr.find_all("td", {"class": "tdesito"})
            if len(td_list) != 0:
                person_info: PersonInfo = self.get_person_info(td_list, name)
                print(f"Found {person_info.full_name}")
                person_info.details = self.get_person_details(person_info)
                # Do not overload the server
                sleep(self.DELAY)

                self.log_person_info(person_info)

    def next_page_exists(self, soup: BeautifulSoup) -> bool:
        matches: List[str] = [
            str(x) for x in list(soup.find_all("a", href=re.compile(r".*tabelle.*")))
        ]
        is_match: bool = False
        for match in matches:
            is_match = is_match or "Successivi" in match
        return is_match

    def log_person_info(self, person_info: PersonInfo) -> None:
        self.db.add_person_info(person_info)

    def scrap(self, names: Set[str]) -> None:
        for name in names:
            print(f"Scraping {name}")
            soup: BeautifulSoup = self.get_first_page(name)
            self.parse_page(name, soup)

            is_next_page: bool = self.next_page_exists(soup)
            i: int = self.MAX_RESULTS_PER_PAGE
            while is_next_page:
                soup = self.get_next_page(page=i)
                self.parse_page(name, soup)
                is_next_page = self.next_page_exists(soup)
                i += self.MAX_RESULTS_PER_PAGE

            # Do not overload the server
            sleep(self.DELAY)
