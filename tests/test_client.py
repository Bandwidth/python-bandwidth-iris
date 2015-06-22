#!/usr/bin/env python

import os
import sys

from unittest import TestCase, main
from unittest.mock import Mock, patch, PropertyMock

if (__package__ == None):
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from iris_sdk.client import Client

class ClassClientInitTest(TestCase):

    """Test class initialization."""

    @classmethod
    def setUpClass(cls):
        with patch('iris_sdk.utils.config.Config'):
            cls._client = Client()

    @classmethod
    def tearDownClass(cls):
        del cls._client

    def test_client_single_instance(self):
        _client1 = Client()
        self.assertIs(self._client, _client1)

    def test_client_config_prop(self):
        self._client._config = "foo"
        self.assertEqual(self._client._config, self._client.config)

class ClassClientConfigTest(TestCase):

    """Test config."""

    @patch('iris_sdk.utils.config.Config.username')
    @patch('iris_sdk.utils.config.Config.password')
    @patch('iris_sdk.utils.rest.RestClient.__init__', return_value=None)
    @patch('iris_sdk.utils.config.Config.__init__', return_value=None)
    def test_client_config_params(self, mock1, mock2, mock3, mock4):
        self._client = Client("foo", "bar", "baz", "qux", "quux")
        mock1.assert_called_once_with("foo", "bar", "baz", "qux", "quux")
        mock2.assert_called_once_with((mock4, mock3))

if __name__ == '__main__':
    main()