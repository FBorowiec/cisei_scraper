from typing import Set

from cisei.cisei_scrapper import CiseiRequestHandler
from cisei.names import get_names_list


def scrap_cisei() -> None:
    cisei_rh: CiseiRequestHandler = CiseiRequestHandler()
    names: Set[str] = get_names_list()

    cisei_rh.scrap(names)


if __name__ == "__main__":
    scrap_cisei()
