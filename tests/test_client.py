#!/usr/bin/env python

import os
import os.path
import sys

import unittest
from unittest.mock import patch

if (__package__ == None):
  sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from iris_sdk.client import Client

class ClassClientInitTest(unittest.TestCase):

    """Test class initialization."""

    @classmethod
    def setUpClass(cls):
        with unittest.mock.patch('iris_sdk.config.Config'):
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

class ClassClientConfigTest(unittest.TestCase):

    """Test config."""

    @patch('iris_sdk.config.Config.__init__', return_value=None)
    def test_client_config_params(self, mock_method):
        self._client = Client("foo", "bar", "baz", "qux")
        mock_method.assert_called_once_with("foo", "bar", "baz", "qux")

if __name__ == '__main__':
    unittest.main()