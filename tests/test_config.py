#!/usr/bin/env python

from io import StringIO
import os
import sys

# For coverage.
if __package__ is None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from iris_sdk.utils.py_compat import PY_VER_MAJOR

from unittest import main, TestCase

if PY_VER_MAJOR == 3:
    from unittest.mock import mock_open, patch, MagicMock
else:
    from mock import mock_open, patch, MagicMock

from iris_sdk.utils.config import *

class ClassConfigPropsTest(TestCase):

    """Test class properties"""

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

class ClassConfigInitializationTest (TestCase) :

    """Test class initialization"""

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

class ClassConfigLoadConfigTest (TestCase) :

    """Test file loading"""

    def setUp(self):
        patcher_isfile = patch("os.path.isfile")
        patcher_getsize = patch("os.path.getsize")
        if PY_VER_MAJOR == 3:
            patcher_config_get = patch(
                'configparser.ConfigParser.get')
            patcher_config_read = patch(
                'configparser.ConfigParser.read_file')
        else:
            patcher_config_get = patch('ConfigParser.ConfigParser.get')
            patcher_config_read = patch('ConfigParser.ConfigParser.readfp')
        self._isfile = patcher_isfile.start()
        self._getsize = patcher_getsize.start()
        self._config_read = patcher_config_read.start()
        self._config_get = patcher_config_get.start()
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
        if PY_VER_MAJOR == 3:
            m.return_value = StringIO("foobar")
        else:
            m.return_value = StringIO(unicode("foobar"))

        self._isfile.return_value = True
        self._getsize.return_value = 0

        self._config_get.side_effect = lambda str1, str2: {
            (SECTION_ACCOUNT, VALUE_ACCOUNT_ID): " foo ",
            (SECTION_ACCOUNT, VALUE_USERNAME): " bar ",
            (SECTION_ACCOUNT, VALUE_PASSWORD): " baz ",
            (SECTION_SRV, VALUE_URL): " qux "} [str1, str2]

        with patch.object(config, "open", m, create=True):
            self._config = Config(filename="whatever")

            self.assertEqual(self._config.account_id, "foo")
            self.assertEqual(self._config.username, "bar")
            self.assertEqual(self._config.password, "baz")
            self.assertEqual(self._config.url, "qux")

if __name__ == "__main__":
    main()