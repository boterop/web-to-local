import requests
import re
from bin.storage import Storage

LOCAL_INDEX_PATH = "/"


class Web:
    def __init__(self, url: str):
        self.index_url = url
        domain = self.get_domain(url)
        self.domain = domain
        self.storage = Storage(domain)

    def get_code(self, path: str = ""):
        url = path if path != "" else self.index_url
        return requests.get(url).text

    def to_code(self, path: str = ""):
        url = path if path != "" else self.index_url
        self.code = requests.get(url).text
        return self

    def convert_to_local(self, code: str = None, current_page: str = None):
        if code == None:
            code = self.code

        if current_page == None:
            current_page = self.index_url

        file_name = (
            re.sub(self.index_url + "/", "", current_page)
            if current_page != self.index_url
            else "index"
        ) + ".html"

        if self.storage.exist(file_name):
            return

        escaped_url = re.escape(current_page)
        sub_links_regex = rf"\b({escaped_url}(?:\/[^\/\s]*)?)\b"
        matches = re.findall(sub_links_regex, code)
        matches = list(filter(lambda url: url != self.index_url, matches))

        escaped_index = re.escape(self.index_url)
        code_without_web_domain = re.sub(
            escaped_index + "/",
            LOCAL_INDEX_PATH,
            code,
        )
        code_without_web_domain = re.sub(
            escaped_index,
            LOCAL_INDEX_PATH,
            code_without_web_domain,
        )

        self.storage.save(file_name, code_without_web_domain)

        for sub_url in matches:
            file_code = self.get_code(sub_url)
            self.convert_to_local(file_code, sub_url)

    def get_domain(self, url: str):
        domain_regex = re.compile(r"^(?:https?:\/\/)?(?:www\.)?([^\/]+)(?:\/.*)?$")
        match = domain_regex.match(url)

        domain = "unknown"
        if match:
            domain = match.group(1)
        return domain
