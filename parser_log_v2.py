from collections import Counter
from pprint import pprint
from typing import List, Callable


class LogParser:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.lines = []
        self._read_file()

    def _read_file(self) -> None:
        with open(self.filename, "r") as file:
            self.lines = file.readlines()

    def get(self, filter_type: Callable) -> List:
        return filter_type(self.lines)

def source_ips(lines) -> List:
    return [elem.split()[0] for elem in lines if elem]

def http_verbs(lines) -> List:
    return [elem.split()[5].replace('"', "") for elem in lines if elem]

def endpoints(lines) -> List:
    return [elem.split()[6] for elem in lines if elem]


if __name__ == "__main__":
    log_parser = LogParser("./access.log")

    ips = log_parser.get(source_ips)

    http_verbs = log_parser.get(http_verbs)
    http_verbs_count = dict(Counter(http_verbs))

    endpoints = log_parser.get(endpoints)
    endpoints_count = dict(Counter(endpoints))

    pprint(ips)
    pprint(http_verbs_count)
    pprint(endpoints_count)
