#!/usr/bin/env python

import os
import sys

# For coverage.
if (__package__ == None):
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from iris_sdk.utils.py_compat import PY_VER_MAJOR

from unittest import main, TestCase

if (PY_VER_MAJOR == 3):
    from unittest.mock import patch, MagicMock, PropertyMock
else:
    from mock import patch, MagicMock, PropertyMock

from iris_sdk.client import Client

class ClassClientInitTest(TestCase):

    """Test class initialization and properties."""

    @classmethod
    def setUpClass(cls):
        with patch("iris_sdk.utils.config.Config"):
            cls._client = Client()

    @classmethod
    def tearDownClass(cls):
        del cls._client

    def test_client_config_prop(self):
        self._client._config = "foo"
        self.assertEqual(self._client._config, self._client.config)

class ClassClientConfigTest(TestCase):

    """Test class config."""

    def setUp(self):
        self._client = None

    def tearDown(self):
        del self._client

    @patch("iris_sdk.utils.rest.RestClient.__init__", return_value = None)
    @patch("iris_sdk.utils.config.Config.__init__", return_value = None)
    def test_client_init(self, mock1, mock2):
        self._client = Client("foo", "bar", "baz", "qux", "quux")
        mock1.assert_called_once_with("foo", "bar", "baz", "qux", "quux")
        mock2.assert_called_once()

class ClassClientStrings(TestCase):

    """Test string manipulation."""

    @classmethod
    def setUpClass(cls):
        with patch("iris_sdk.utils.config.Config"):
            with patch("iris_sdk.utils.rest.RestClient"):
                cls._client = Client("foo///")

    @classmethod
    def tearDownClass(cls):
        del cls._client

    def test_client_get_uri_no_section(self):
        str = self._client._get_uri()
        self.assertEqual(str, "foo")

    def test_client_get_uri_with_section(self):
        str = self._client._get_uri("///bar/baz///")
        self.assertEqual(str, "foo/bar/baz")

class ClassClientRequests(TestCase):

    """Test rest requests."""

    def setUp(self):

        patcher_req = patch("iris_sdk.utils.rest.RestClient.request")
        patcher_url = patch("iris_sdk.utils.config.Config.url",
            new_callable = PropertyMock, return_value = "foo")
        patcher_pass = patch("iris_sdk.utils.config.Config.password",
            new_callable = PropertyMock, return_value = "bar")
        patcher_user = patch("iris_sdk.utils.config.Config.username",
            new_callable = PropertyMock, return_value = "baz")

        self._url = patcher_url.start()
        self._pass = patcher_pass.start()
        self._request = patcher_req.start()
        self._user = patcher_user.start()

        self._request.return_value = self._mock_res

        self.addCleanup(patch.stopall)

    @classmethod
    def setUpClass(cls):

        cls._mock_res = MagicMock("requests.models.Request")
        cls._mock_res.headers = {"location": "return/return1"}
        cls._mock_res.content = b"foobar"
        cls._mock_res.status_code = 1337

        with patch("iris_sdk.utils.config.Config"):
            with patch("iris_sdk.utils.rest.RestClient"):
                cls._client = Client()

    @classmethod
    def tearDownClass(cls):
        del cls._client

    def test_client_delete(self):
        res = self._client.delete("qux")
        self._request.assert_called_once_with("DELETE",
            url="foo/qux", data=None,
            auth=(self._user.return_value, self._pass.return_value),
            params=None)

    def test_client_get(self):
        res = self._client.get("", "qux")
        self._request.assert_called_once_with("GET", data=None,
            auth=(self._user.return_value, self._pass.return_value),
            params="qux", url=self._url.return_value,)

    def test_client_post(self):
        res = self._client.post("", "qux", "quux")
        self._request.assert_called_once_with("POST",
            auth=(self._user.return_value, self._pass.return_value),
            url=self._url.return_value, params="qux", data="quux")

    def test_client_put(self):
        self._request.return_value.status_code = 200
        res = self._client.put("", "qux", "quux")
        self._request.assert_called_once_with("PUT",
            url=self._url.return_value, data="quux", 
            auth=(self._user.return_value, self._pass.return_value),
            params="qux")

if __name__ == "__main__":
    main()