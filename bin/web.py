import requests
import re
from bin.storage import Storage


class Web:
    def __init__(self, url: str):
        self.url = url
        domain = self.get_domain(url)
        self.domain = domain
        self.storage = Storage(domain)

    def get_code(self):
        return requests.get(self.url).text

    def to_code(self):
        self.code = requests.get(self.url).text
        return self

    def convert_to_local(self, code: str = None):
        if code == None:
            code = self.code

        new_code = self._convert_links(self.code)
        self.storage.save("index.html", new_code)

    def get_domain(self, url: str):
        domain_regex = re.compile(r"^(?:https?:\/\/)?(?:www\.)?([^\/]+)(?:\/.*)?$")
        match = domain_regex.match(url)

        domain = "unknown"
        if match:
            domain = match.group(1)
        return domain

    def _convert_links(self, code: str):
        new_code = re.sub(
            self.url,
            "/",
            code,
        )
        return new_code
