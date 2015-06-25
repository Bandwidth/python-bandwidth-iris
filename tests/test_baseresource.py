#!/usr/bin/env python

import os
import sys

from iris_sdk.utils.py_compat import PY_VER_MAJOR

from unittest import TestCase, main

if (PY_VER_MAJOR == 3):
    from unittest.mock import patch, mock_open
else:
    from mock import patch, mock_open

if (__package__ == None):
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from iris_sdk.models.resource import BaseResource

FOO_XML = (
    "<FooBar>"
    "    <Baz>"
    "        <QuxQuux>0</QuxQuux>"
    "        <GarplyWaldo></GarplyWaldo>"
    "        <Fred>"
    "            <Barney>1</Barney>"
    "            <Barney>1</Barney>"
    "        </Fred>"
    "    </Baz>"
    "</FooBar>"
)

class ClassBaseResourceInitTest(TestCase):

    """Test class initialization and properties."""

    def setUp(self):
        _patcher = patch("iris_sdk.utils.strings.Converter.__init__",
            return_value=None)
        self._converter = _patcher.start()
        self.addCleanup(patch.stopall)

    def test_baseresource_init(self):

        self._base_resource = BaseResource("foo", "bar")

        self._converter.assert_called_once()
        self.assertEqual(self._base_resource._client, "foo")
        self.assertEqual(self._base_resource._xpath, "bar")

        del self._base_resource

        self._base_resource = BaseResource("foo")
        self.assertEqual(self._base_resource._xpath, "")

class ClassPropsTest(TestCase):

    """Test class properties."""

    def setUp(self):
        patcher = patch("iris_sdk.utils.strings.Converter.__init__",
            return_value=None)
        self._converter = patcher.start()
        self.addCleanup(patch.stopall)
        self._base_resource = BaseResource("foo", "bar")

    def tearDown(self):
        del self._base_resource

    def test_baseresource_client_prop(self):
        self._base_resource.client = "foo"
        self.assertEqual(self._base_resource._client, "foo")
        self.assertEqual(self._base_resource._client,
            self._base_resource.client)

    def test_baseresource_xpath_prop(self):
        self._base_resource._xpath = "foo"
        self.assertEqual(self._base_resource.xpath, "foo")

class ClassGetTest(TestCase):

    """Test getting server responses"""

    def setUp(self):
        patcher_init = patch(
            "iris_sdk.utils.strings.Converter.__init__", return_value=None)
        self._init_patched = patcher_init.start()
        self.addCleanup(patch.stopall)

    @patch("iris_sdk.client.Client.get", return_value="jim")
    @patch("xml.etree.ElementTree.fromstring", return_value="barney")
    @patch("iris_sdk.models.resource.BaseResource._parse_xml")
    def test_raw_get(self, parse_patched, fs_patched, get_patched):

        _base_resource = BaseResource("foo", "bar")
        _base_resource.client = MagicMock(spec="iris_sdk.client.Client")
        _base_resource.client.config = MagicMock(
            spec="iris_sdk.utils.config.Config")

        _base_resource.client.get = get_patched
        _base_resource._xpath = "{} fred {}"
        _base_resource.client.config.account_id = "qux"

        res = _base_resource.get_raw("quux", "garply", "waldo")

        get_patched.assert_called_once_with("qux fred quux", "garply")
        fs_patched.assert_called_once_with("jim")
        parse_patched.assert_called_once_with(
            element="barney", classname="waldo")
        self.assertEqual(res, _base_resource)

    @patch("iris_sdk.utils.strings.Converter.to_camelcase",return_value="jim")
    def test_raw_get(self, camel_patched):
        pass

if __name__ == "__main__":
    main()