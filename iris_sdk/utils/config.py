#!/usr/bin/env python

from future import standard_library

import os

from iris_sdk.utils.py_compat import PY_VER_MAJOR

if PY_VER_MAJOR < 3:
    from io import open

from configparser import ConfigParser

MAX_FILE_SIZE = 1048576
SECTION_ACCOUNT = "account"
SECTION_SRV = "rest"
VALUE_ACCOUNT_ID = "account_id"
VALUE_PASSWORD = "password"
VALUE_URL = "url"
VALUE_USERNAME = "username"

class ConfigData(object):

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

class Config(ConfigData):

    """Connection and auth settings"""

    def __init__(
            self, url=None, account_id=None, username=None, password=None,
            filename=None):

        if filename is None:
            self._account_id = account_id
            self._password = password
            self._url = url
            self._username = username
        else:
            self._account_id = None
            self._password = None
            self._url = None
            self._username = None
            self.load_from_file(filename)

    def load_from_file(self, filename=None):

      """
      Loads config values from "filename".

      See the default file for structure.
      Configs larger than MAX_FILE_SIZE are skipped.
      Leading and trailing whitespace is removed.

      Args:
          filename: a UTF-8 config file.
      """

      # Skip non-existing and huge files

      if not os.path.isfile(filename):
          raise ValueError("Config file doesn't exist")

      if os.path.getsize(filename) > MAX_FILE_SIZE:
          raise ValueError("Config too large")

      with open(filename, encoding="UTF-8") as fp:
          self._parser = ConfigParser(allow_no_value = True)
          if PY_VER_MAJOR == 3:
              self._parser.read_file(fp)
          else:
              self._parser.readfp(fp)

      self._account_id = self._parser.get(
        SECTION_ACCOUNT, VALUE_ACCOUNT_ID
      )
      self._account_id = self._account_id.strip()

      self._username = self._parser.get(SECTION_ACCOUNT, VALUE_USERNAME)
      self._username = self._username.strip()

      self._password = self._parser.get(SECTION_ACCOUNT, VALUE_PASSWORD)
      self._password = self._password.strip()

      self._url = self._parser.get(SECTION_SRV, VALUE_URL)
      self._url = self._url.strip()