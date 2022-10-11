import csv
from typing import List, Set


def get_names(path: str) -> List[str]:
    names_list: List[str] = []
    with open(path, mode="r") as f:
        names = csv.reader(f)
        for name in names:
            names_list.append(name[0])

    return names_list


def get_names_list() -> Set[str]:
    italian_names_list: List[str] = get_names("cognomix/names.csv")
    jewish_names_list: List[str] = get_names("cognomix/jewish_italian_names.csv")

    return sorted(set(italian_names_list + jewish_names_list))
