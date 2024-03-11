import requests
import re
from bin.storage import Storage


class Web:
    def __init__(self, url):
        self.url = url
        self.storage = Storage(self.get_domain(url))

    def get_code(self):
        return requests.get(self.url).text

    def to_code(self):
        self.code = requests.get(self.url).text
        return self

    def convert_to_local(self, code=None):
        if code == None:
            code = self.code

        self.storage.save("index.html", code)

    def get_domain(self, url):
        domain_regex = re.compile(r"^(?:https?:\/\/)?(?:www\.)?([^\/]+)(?:\/.*)?$")
        match = domain_regex.match(url)

        domain = "unknown"
        if match:
            domain = match.group(1)
        return domain
