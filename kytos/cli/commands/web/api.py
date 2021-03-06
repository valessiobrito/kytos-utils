"""Translate cli commands to non-cli code."""
import logging
from urllib.error import HTTPError, URLError

import requests

from kytos.utils.config import KytosConfig

LOG = logging.getLogger(__name__)


class WebAPI:  # pylint: disable=too-few-public-methods
    """An API for the command-line interface."""

    @classmethod
    def update(cls):
        """Call the method to update the Web UI."""
        kytos_api = KytosConfig().config.get('kytos', 'api')
        url = f"{kytos_api}api/kytos/core/web/update/"
        try:
            result = requests.post(url)
        except(HTTPError, URLError, requests.exceptions.ConnectionError):
            LOG.error(f"Can't connect to the server: {kytos_api}")
            return

        if result.status_code != 200:
            LOG.info(f"Error while update web ui: {result.content}")
        else:
            LOG.info("Web UI updated.")
