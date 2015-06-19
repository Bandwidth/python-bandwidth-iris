#!/usr/bin/env python

import os
import os.path

import configparser

MAX_FILE_SIZE = 1048576
SECTION_ACCOUNT = "account"
VALUE_ACCOUNT_ID = "account_id"
VALUE_PASSWORD = "password"
VALUE_USERNAME = "username"

class Config:

    """Reads config settings."""

    def __init__(
            self, account_id=None, username=None, password=None,
            filename=None):

        if (filename is None):
            self.account_id = account_id
            self.password = password
            self.username = username
        else:
            self.account_id = None
            self.password = None
            self.username = None
            self.load_from_file(filename)

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
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    def load_from_file(self, filename=None):

      """
      Loads config values from "filename".

      See the default file for structure.
      Configs larger than MAX_FILE_SIZE are skipped.
      Leading and trailing whitespace is removed.
      If no file is specified, CONFIG_VAR is read instead.

      Args:
          filename: a UTF-8 config file.
      """

      # Skip non-existing and huge files.

      if (not os.path.isfile(filename)):
          raise ValueError("Config file doesn't exist")

      if os.path.getsize(filename) > MAX_FILE_SIZE:
          raise ValueError("Config too large")

      with open(filename, encoding = "UTF-8") as fp:
          self._parser = configparser.ConfigParser(allow_no_value = True)
          self._parser.read_file(fp)

      self._account_id = self._parser.get(
        SECTION_ACCOUNT, VALUE_ACCOUNT_ID
      )
      self._account_id = self._account_id.strip()

      self._username = self._parser.get(SECTION_ACCOUNT, VALUE_USERNAME)
      self._username = self._username.strip()

      self._password = self._parser.get(SECTION_ACCOUNT, VALUE_PASSWORD)
      self._password = self._password.strip()