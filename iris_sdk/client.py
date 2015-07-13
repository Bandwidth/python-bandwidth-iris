#!/usr/bin/env python

from iris_sdk.utils.config import Config
from iris_sdk.utils.rest import RestClient

class Client(object):

    """Data fetching"""

    @property
    def config(self):
        return self._config

    def __init__(
            self, url=None, account_id=None, username=None, password=None,
            filename=None):

        self._config = Config(url, account_id, username, password, filename)
        self._rest = RestClient()

    def _get_uri(self, section=None):

        """http://foo/bar/// + ///bar/// -> http://foo/bar"""

        _section = ""
        if section is not None:
            _section = section.lstrip('/').rstrip('/')

        res = self.config.url.rstrip('/') + ("" if not _section else '/') + \
            _section

        return res

    def _request(self, method, section=None, params=None, data=None):
        return self._rest.request(
                    method, url=self._get_uri(section),
                    auth=(self.config.username, self.config.password),
                    params=params, data=data)

    def delete(self, section=None):
        return self._request("DELETE", section)

    def get(self, section=None, params=None):
        return self._request("GET", section, params)

    def post(self, section=None, params=None, data=None):
        return self._request("POST", section, params, data)

    def put(self, section=None, params=None, data=None):
        return self._request("PUT", section, params, data)