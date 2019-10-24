import requests
import json

from urlbuilder import URLBuilder
import exceptions


class WebDAO:
    """Data access object responsible for accessing CPSC Rest API"""
    response = None
    __url = None

    def set_download_url(self, url: str):
        self.__url = url
        return self

    def download(self):
        self.response = requests.get(self.__url)
        if self.response.status_code != 200:
            raise exceptions.RestApiQueryError(
                f"Code {self.response.status_code} error")

    def get_raw_content(self):
        return self.response.content
