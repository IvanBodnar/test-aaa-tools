from urllib.parse import urljoin

import requests
from requests import Response
from requests.exceptions import RequestException

from .exceptions import RequestsError


class HttpClient:
    def __init__(self, base_url: str = ''):
        self._base_url = base_url

    def send(self, url: str, method: str = 'GET', **kwargs) -> Response:
        url = urljoin(self._base_url, url)
        try:
            return requests.request(method=method, url=url, **kwargs)
        except RequestException as e:
            raise RequestsError(str(e))
