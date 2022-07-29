#!/usr/bin/env python

import os
import sys

# For coverage.
if __package__ is None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from iris_sdk.utils.py_compat import PY_VER_MAJOR

from unittest import main, TestCase

if PY_VER_MAJOR == 3:
    from unittest.mock import MagicMock, patch
else:
    from mock import MagicMock, patch

from requests.exceptions import HTTPError

from iris_sdk.utils.rest import ERROR_TAG, ERROR_TEMPLATE, HEADERS, HTTP_OK,\
    RestClient, RestError

class HttpErrorStub(HTTPError):
    pass

class ClassRestRequestTest(TestCase):

    """Test HTTP requests"""

    def raise_for_status_stub(self):
        raise HttpErrorStub("foo")

    @classmethod
    def setUpClass(cls):
        cls._mock_req_res = MagicMock("requests.models.Response")
        cls._mock_req_res.status_code = HTTP_OK
        cls._mock_req_res.headers = {"foo": "bar"}
        cls._rest_client = RestClient()

    def setUp(self):
        patcher_req = patch("requests.request")
        patcher_resp = patch("requests.Response")
        patcher_stat = patch("requests.Response.raise_for_status")

        self._resp = patcher_resp.start()
        self._request = patcher_req.start()
        self._stat = patcher_stat.start()
        self._request.return_value = self._mock_req_res

        self.addCleanup(patch.stopall)

    @classmethod
    def tearDownClass(cls):
        del cls._rest_client

    def test_rest_client_request_wrong_method(self):
        with self.assertRaises(AssertionError):
            self._rest_client.request("foo", "bar", "baz")

    def test_rest_client_response(self):

        self._mock_req_res.content=b"<something><foo>bar</foo><baz>qux</baz>"
        self._mock_req_res.status_code = HTTP_OK
        self._mock_req_res.raise_for_status = self._stat

        self._rest_client.request("GET","foo","bar","baz","qux")
        self._request.assert_called_once_with("GET", "foo", auth="bar",
            headers=HEADERS, params="baz", data="qux")
        self._stat.assert_any_call

        self.assertEqual(self._mock_req_res.status_code, HTTP_OK)
        self.assertEqual(self._mock_req_res.content,
            b"<something><foo>bar</foo><baz>qux</baz>")
        self.assertEqual(self._mock_req_res.headers["foo"], "bar")

    # @patch("xml.etree.ElementTree.fromstring", return_value = "foo")
    # def test_rest_client_exception(self, _fromstring):

    #     class XmlElem(object):
    #         def __init__(self):
    #             self.find_res = None
    #             self.children = []
    #             self.tag = None
    #             self.text = None
    #         def find(self, str):
    #             self._call_arg = str
    #             return self.find_res
    #         def getchildren(self):
    #             return self.children

    #     self._mock_req_res.content = b""
    #     self._mock_req_res.status_code = 300
    #     self._mock_req_res.raise_for_status = self.raise_for_status_stub

    #     with self.assertRaises(HttpErrorStub):
    #         self._rest_client.request("GET","foo","bar","baz","qux")

    #     self._mock_req_res.content =b"<something><foo>bar</foo><baz>qux</baz>"

    #     _mock = [[0 for i in range(2)] for i in range(1)]

    #     _m = XmlElem()
    #     _n = XmlElem()
    #     _m.text = "bar"
    #     _n.text = "qux"
    #     _mock[0][0] = _m
    #     _mock[0][1] = _n

    #     root = XmlElem()
    #     root.find_res = _mock
    #     _fromstring.return_value = root

    #     if PY_VER_MAJOR == 3:
    #         with self.assertRaisesRegex(RestError,
    #                 ERROR_TEMPLATE.format("bar", "qux")):
    #             self._rest_client.request("GET","foo","bar","baz","qux")
    #     else:
    #         with self.assertRaisesRegexp(RestError,
    #                 ERROR_TEMPLATE.format("bar", "qux")):
    #             self._rest_client.request("GET","foo","bar","baz","qux")

    #     root.find_res = None
    #     root.children = [_m, _n]

    #     if PY_VER_MAJOR == 3:
    #         with self.assertRaisesRegex(RestError,
    #                 "<something><foo>bar</foo><baz>qux</baz>"):
    #             self._rest_client.request("GET","foo","bar","baz","qux")
    #     else:
    #         with self.assertRaisesRegexp(RestError,
    #                 "<something><foo>bar</foo><baz>qux</baz>"):
    #             self._rest_client.request("GET","foo","bar","baz","qux")

    #     _m.find_res = _mock

    #     if PY_VER_MAJOR == 3:
    #         with self.assertRaisesRegex(RestError,
    #                 ERROR_TEMPLATE.format("bar", "qux")):
    #             self._rest_client.request("GET","foo","bar","baz","qux")
    #     else:
    #         with self.assertRaisesRegexp(RestError,
    #                 ERROR_TEMPLATE.format("bar", "qux")):
    #             self._rest_client.request("GET","foo","bar","baz","qux")

if __name__ == "__main__":
    main()