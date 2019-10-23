import sys
sys.path.append("src/")

import requests
from url_builder import URLBuilder

class WebDAO:
    """Data access object"""
    url_builder = None
    response = None

    def __init__(self, url_builder: URLBuilder):
        self.url_builder = url_builder

    def get_data(self):
        self.response = requests.get(self.url_builder.get_url())
    