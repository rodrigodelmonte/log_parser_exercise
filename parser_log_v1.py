"""
❯ python parser_log_v1.py
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
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.lines = []
        self._read_file()

    def _read_file(self):
        with open(self.filename, "r") as file:
            self.lines = file.readlines()

    def get_source_ips(self) -> List:
        return [elem.split()[0] for elem in self.lines if elem]

    def get_http_verb(self) -> List:
        return [elem.split()[5].replace('"', "") for elem in self.lines if elem]

    def get_endpoints(self) -> List:
        return [elem.split()[6] for elem in self.lines if elem]


if __name__ == "__main__":
    log_parser = LogParser("./access.log")

    ips = log_parser.get_source_ips()

    http_verbs = log_parser.get_http_verb()
    http_verbs_count = dict(Counter(http_verbs))

    endpoints = log_parser.get_endpoints()
    endpoints_count = dict(Counter(endpoints))

    pprint(ips)
    pprint(http_verbs_count)
    pprint(endpoints_count)
