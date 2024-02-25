"""
❯ python parser_log_v4.py
['146.133.3.54',
 '49.40.115.237',
 '106.57.154.56',
 '90.201.104.250',
 '206.150.204.239',
 '254.66.78.26',
 '254.109.239.86',
 '72.170.167.151',
 '178.223.45.74',
 '135.187.2.113']
{'DELETE': 2, 'GET': 2, 'HEAD': 4, 'PUT': 2}
{'/about': 2, '/contact': 2, '/logout': 2, '/products': 4}
"""

from collections import Counter
from pprint import pprint
from typing import List


class LogParser:

    filters = []

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.lines = []
        self._read_file()

    def _read_file(self) -> None:
        with open(self.filename, "r") as file:
            self.lines = file.readlines()

    def __call__(self):
        for _filter in self.filters:
            _filter(self.lines)

    @classmethod
    def add_filter(cls, field):
        cls.filters.append(field)
        return field


@LogParser.add_filter
def source_ips(lines) -> List:
    pprint([elem.split()[0] for elem in lines if elem])


@LogParser.add_filter
def http_verbs(lines) -> List:
    pprint(dict(Counter([elem.split()[5].replace('"', "") for elem in lines if elem])))


@LogParser.add_filter
def endpoints(lines) -> List:
    pprint(dict(Counter([elem.split()[6] for elem in lines if elem])))


if __name__ == "__main__":
    log_parser = LogParser("./access.log")
    log_parser()
