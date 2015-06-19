#!/usr/bin/env python

import os
import os.path
import sys

import unittest
from unittest.mock import patch

if (__package__ == None):
  sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from iris_sdk.config import *

# A valid config.
FILE_TEST_CFG =(
    "\n[" + SECTION_ACCOUNT + "]" + "\n" +
    VALUE_ACCOUNT_ID + " = \u28F1 foo \n" + # U+10481, Ba
    VALUE_USERNAME + " =  baz " + "\n" + # Leading and trailing ws
    VALUE_PASSWORD + " = \nbar " + "\n" # Supposed to be empty
)

class ClassPropsTest(unittest.TestCase):

    """Test class properties."""

    @classmethod
    def setUpClass(cls):
        cls._config = Config()

    @classmethod
    def tearDownClass(cls):
        del cls._config

    def test_config_prop_account_id(self):
        self._config._account_id = "foo"
        self.assertEqual(self._config._account_id, "foo")
        self.assertEqual(self._config._account_id, self._config.account_id)

    def test_config_prop_password(self):
        self._config._password = "bar"
        self.assertEqual(self._config._password, "bar")
        self.assertEqual(self._config._password, self._config.password)

    def test_config_prop_username(self):
        self._config._username = "baz"
        self.assertEqual(self._config._username, "baz")
        self.assertEqual(self._config._username, self._config.username)

class ClassInitializationTest ( unittest.TestCase ) :

    """Test class initialization."""

    @patch('iris_sdk.config.Config.load_from_file')
    def test_config__init_without_filename(self, mock_method):
        self._config = Config("foo", "bar", "baz")
        self.assertEqual(self._config.account_id, "foo" )
        self.assertEqual(self._config.password, "baz" )
        self.assertEqual(self._config.username, "bar" )
        assert not mock_method.called

    @patch('iris_sdk.config.Config.load_from_file')
    def test_config__init_with_filename(self, mock_method):
        self._config = Config("foo", "bar", "baz", "qux")
        self.assertEqual(self._config.account_id, None )
        self.assertEqual(self._config.password, None )
        self.assertEqual(self._config.username, None )
        mock_method.assert_called_once_with("qux")

class ClassLoadCOnfigTest ( unittest.TestCase ) :

    """Test file loading."""

    def test_config_load_from_non_existing_file(self):
        with unittest.mock.patch('os.path.isfile',return_value=False) as func:
            with self.assertRaises(ValueError):
                self._config = Config("foo", "bar", "baz", "qux")

    def test_config_load_from_huge_file(self):
        with unittest.mock.patch('os.path.getsize',
                return_value = MAX_FILE_SIZE + 1):
            with unittest.mock.patch('os.path.isfile', return_value=True):
                with self.assertRaises(ValueError):
                    self._config = Config("foo", "bar", "baz", "qux")

    def test_config_load_from_good_file(self):
        with open("./tests/fixtures/test_cfg","w+",encoding="UTF-8") as test:
            test.write(FILE_TEST_CFG)
        self.assertTrue(test.closed)
        self._config = Config(
            "foo", "bar", "baz", "./tests/fixtures/test_cfg")
        self.assertEqual(self._config.account_id, "\u28F1 foo")
        self.assertEqual(self._config.username, "baz")
        self.assertEqual(self._config.password, "")
        os.remove("./tests/fixtures/test_cfg")

if __name__ == '__main__':
    unittest.main()