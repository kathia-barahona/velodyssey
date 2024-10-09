from logging import Logger

import requests
from requests.exceptions import RequestException


class BaseClient:
    API_BASE_URL = ""

    def __init__(self, logging: Logger):
        self.session = requests.Session()
        self.logging = logging

    def _get_headers(self) -> dict[str, str]:
        raise NotImplementedError

    def get(self, path: str, params: dict = None) -> requests.Response:
        headers = self._get_headers()
        url = f"{self.API_BASE_URL}{path}"
        try:
            response = self.session.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response
        except RequestException:
            self.logging.error(f"Failed when requesting {url}.")
            raise

    def post(self):
        ...
