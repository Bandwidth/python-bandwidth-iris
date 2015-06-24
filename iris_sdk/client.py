#!/usr/bin/env python

from iris_sdk.utils.config import Config
from iris_sdk.utils.rest import RestClient, HTTP_OK

class Client():

    """Data fetching"""

    def __init__(
            self, url=None, account_id=None, username=None, password=None,
            filename=None):

        self._config = Config(url, account_id, username, password, filename)
        self._rest = RestClient()

    @property
    def config(self):
        return self._config

    def delete(self, section=None, params=None):
        res = (self._rest.request(
                    "DELETE", self.get_uri(section),
                    (self.config.username, self.config.password), params
                ).status_code == HTTP_OK)
        return res

    def get(self, section=None, params=None):
        print(section)
        _params = {}
        _params["accountId"] = self.config.account_id
        return self._rest.request(
                    "GET", url=self.get_uri(section),
                    auth=(self.config.username, self.config.password),
                    params=_params
                ).content.decode(encoding="UTF-8")

    def get_uri(self, section=None):
        # http://foo/bar/// + ///bar/// -> http://foo/bar
        _section = ""
        if (section is not None):
            _section = section.lstrip('/').rstrip('/')
        res = self.config.url.rstrip('/') + ("" if not _section else '/') + \
            _section
        return res

    def post(self, section=None, params=None, data=None):
        location = self._rest.request(
                    "POST", self.get_uri(section),
                    (self.config.username,self.config.password), params, data
                ).headers["location"]
        res = ""
        if (location is not None):
            pos = location.rfind("/")
            res = location[pos+1:]
        return res

    def put(self, section=None, params=None, data=None):
        res = (self._rest.request(
                    "PUT", self.get_uri(section),
                    (self.config.username, self.config.password), params, data
                ).status_code == HTTP_OK)
        return res