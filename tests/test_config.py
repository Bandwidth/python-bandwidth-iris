#!/usr/bin/env python

from io import StringIO
import os
import sys

from iris_sdk.utils.py_compat import PY_VER_MAJOR

from unittest import TestCase, main

if (PY_VER_MAJOR == 3):
    from unittest.mock import patch, mock_open
else:
    from mock import patch, mock_open

# For coverage
if (__package__ == None):
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from iris_sdk.utils.config import *

# A valid config.
FILE_TEST_CFG =(
    "[" + SECTION_ACCOUNT + "]\n" +
    VALUE_ACCOUNT_ID + " = \u28F1 foo \n" + # U+10481, Ba
    VALUE_USERNAME + " =  baz " + "\n" + # Leading and trailing ws
    VALUE_PASSWORD + " = \nbar " + "\n" + # Supposed to be empty
    "[" + SECTION_SRV + "]\n" +
    VALUE_URL + " = qux"
)

class ClassPropsTest(TestCase):

    """Test class properties."""

    @classmethod
    def setUpClass(cls):
        cls._config = Config()

    @classmethod
    def tearDownClass(cls):
        del cls._config

    def test_config_prop_account_id(self):
        self._config.account_id = "foo"
        self.assertEqual(self._config._account_id, "foo")
        self.assertEqual(self._config._account_id, self._config.account_id)

    def test_config_prop_password(self):
        self._config.password = "bar"
        self.assertEqual(self._config._password, "bar")
        self.assertEqual(self._config._password, self._config.password)

    def test_config_prop_url(self):
        self._config.url = "baz"
        self.assertEqual(self._config._url, self._config.url)
        self.assertEqual(self._config._url, "baz")

    def test_config_prop_username(self):
        self._config.username = "qux"
        self.assertEqual(self._config._username, self._config.username)
        self.assertEqual(self._config._username, "qux")

class ClassInitializationTest (TestCase) :

    """Test class initialization."""

    def setUp(self):
        patcher = patch("iris_sdk.utils.config.Config.load_from_file")
        self._patch = patcher.start()
        self.addCleanup(patch.stopall)

    def test_config__init_without_filename(self):
        self._config = Config("foo", "bar", "baz", "qux")
        self.assertEqual(self._config.url, "foo" )
        self.assertEqual(self._config.account_id, "bar" )
        self.assertEqual(self._config.username, "baz" )
        self.assertEqual(self._config.password, "qux" )
        assert not self._patch.called

    def test_config__init_with_filename(self):
        self._config = Config("foo", "bar", "baz", "qux", "quux")
        self.assertEqual(self._config.url, None )
        self.assertEqual(self._config.account_id, None )
        self.assertEqual(self._config.password, None )
        self.assertEqual(self._config.username, None )
        self._patch.assert_called_once_with("quux")

class ClassLoadConfigTest (TestCase) :

    """Test file loading."""

    def setUp(self):
        patcher_isfile = patch("os.path.isfile")
        patcher_getsize = patch("os.path.getsize")
        self._isfile = patcher_isfile.start()
        self._getsize = patcher_getsize.start()
        self.addCleanup(patch.stopall)

    def test_config_load_from_non_existing_file(self):
        self._isfile.return_value = False
        with self.assertRaises(ValueError):
            self._config = Config(filename="foo")

    def test_config_load_from_huge_file(self):
        self._isfile.return_value = True
        self._getsize.return_value = MAX_FILE_SIZE + 1
        with self.assertRaises(ValueError):
            self._config = Config(filename="foo")

    def test_config_load_from_good_file(self):

        from iris_sdk.utils import config

        m = mock_open()
        m.return_value = StringIO(unicode(FILE_TEST_CFG))

        self._isfile.return_value = True
        self._getsize.return_value = 0

        with patch.object(config, "open", m, create=True):
            self._config = Config(filename="whatever")
            self.assertEqual(self._config.account_id, "\u28F1 foo")
            self.assertEqual(self._config.username, "baz")
            self.assertEqual(self._config.password, "")

if __name__ == "__main__":
    main()