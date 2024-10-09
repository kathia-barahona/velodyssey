from logging import Logger

import requests
from requests.exceptions import RequestException


class BaseClient:
    API_BASE_URL = ""
    TIMEOUT = 60

    def __init__(self, logging: Logger):
        self.session = requests.Session()
        self.logging = logging

    def _get_headers(self) -> dict[str, str]:
        raise NotImplementedError

    def get(self, path: str, params: dict | None = None) -> requests.Response:
        headers = self._get_headers()
        url = f"{self.API_BASE_URL}{path}"

        try:
            response = self.session.get(
                url, params=params, headers=headers, timeout=self.TIMEOUT,
            )
            response.raise_for_status()
            return response
        except RequestException:
            self.logging.error(f"Failed when requesting {url}.")
            raise

    def post(self, path: str, data: dict | None = None) -> requests.Response:
        url = f"{self.API_BASE_URL}{path}"
        headers = self._get_headers()
        try:
            response = self.session.post(url, data=data, headers=headers)
            response.raise_for_status()
            return response
        except RequestException as e:
            self.logging.error(f"Error during POST request: {e}")
            raise
