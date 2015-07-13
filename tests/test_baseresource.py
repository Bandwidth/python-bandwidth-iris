#!/usr/bin/env python

import os
import sys

# For coverage.
if (__package__ == None):
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from iris_sdk.utils.py_compat import PY_VER_MAJOR

from unittest import main, TestCase

if (PY_VER_MAJOR == 3):
    from unittest.mock import call, MagicMock, patch
else:
    from mock import call, MagicMock, patch

from iris_sdk.models.base_resource import BaseResource

class ContentStub(object):
    content = None

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
        self.assertEqual(self._base_resource._parent, "foo")
        self.assertEqual(self._base_resource._client, "bar")

        del self._base_resource

        self._base_resource = BaseResource("foo")
        self.assertEqual(self._base_resource._parent, "")

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
        patcher_fromstring = patch("xml.etree.ElementTree.fromstring",
            return_value = "barney")
        self._init_patched = patcher_init.start()
        self.fs_patched = patcher_fromstring.start()
        self.addCleanup(patch.stopall)

    @patch("iris_sdk.client.Client.get")
    @patch("iris_sdk.models.base_resource.BaseResource._from_xml")
    def test_raw_get(self, parse_patched, get_patched):

        _base_resource = BaseResource(client="bar")
        _base_resource.client = MagicMock(spec="iris_sdk.client.Client")
        _base_resource.client.config = MagicMock(
            spec="iris_sdk.utils.config.Config")

        get_patched.return_value = ContentStub()
        get_patched.return_value.content = bytes("jim", encoding="UTF-8")

        _base_resource.client.get = get_patched
        _base_resource._xpath = "fred {}"
        _base_resource.client.config.account_id = "qux"

        res = _base_resource._get("garply", "waldo")

        get_patched.assert_called_once_with("fred garply", "waldo")

    @patch("iris_sdk.utils.strings.Converter.to_camelcase",return_value="Baz")
    @patch("iris_sdk.utils.strings.Converter.to_underscore")
    def test_parse_xml(self, under_patched, camel_patched):

        class Baz(BaseResource):
            def __init__(self, client=None, xpath=None):
                super().__init__(client=client)
                self._fred = Fred()
                self._qux_quux = None
                self._garply_waldo = None
                self._xpath=xpath
            @property
            def fred(self):
                return self._fred
            @property
            def qux_quux(self):
                return self._qux_quux
            @qux_quux.setter
            def qux_quux(self, qux_quux):
                self._qux_quux = qux_quux
            @property
            def garply_waldo(self):
                return self._garply_waldo
            @garply_waldo.setter
            def garply_waldo(self, garply_waldo):
                self._garply_waldo = garply_waldo

        class Fred(object):
            def __init__(self):
                self._items = []
            @property
            def items(self):
                return self._items
            def barney(self):
                return self.items

        class xml_elem(object):
            def __init__(self):
                self.lst = []
                self.children = []
                self.tag = None
                self.text = None
            def findall(self, str):
                self._call_arg = str
                return self.lst
            def getchildren(self):
                return self.children

        under_patched.side_effect = lambda str: {
            "QuxQuux": "qux_quux", "GarplyWaldo": "garply_waldo",
            "JimSheila": "jim_sheila", "Fred": "fred",
            "Barney": "barney", "Baz": "baz", "FooBar": "foo_bar"} [str]

        # <FooBar>
        #     <Baz>
        #         <QuxQuux>0</QuxQuux>
        #         <GarplyWaldo></GarplyWaldo>
        #         <JimSheila>123</JimSheila> - the class doesn't have this
        #         <Fred>
        #             <Barney>1</Barney>
        #             <Barney>2</Barney>
        #         </Fred>
        #     </Baz>
        # </FooBar>

        _xml_root = xml_elem()
        _xml_resource = xml_elem()

        _xml_elem_sub1 = xml_elem()
        _xml_elem_sub2 = xml_elem()
        _xml_elem_sub3 = xml_elem()
        _xml_elem_sub4 = xml_elem()

        _xml_elem_sub_sub1 = xml_elem()
        _xml_elem_sub_sub2 = xml_elem()

        _xml_elem_sub1.tag = "QuxQuux"
        _xml_elem_sub1.text = "0"

        _xml_elem_sub2.tag = "GarplyWaldo"

        _xml_elem_sub3.tag = "JimSheila"
        _xml_elem_sub3.text = "123"

        _xml_elem_sub4.tag = "Fred"

        _xml_elem_sub_sub1.tag = "Barney"
        _xml_elem_sub_sub1.text = "1"

        _xml_elem_sub_sub2.tag = "Barney"
        _xml_elem_sub_sub2.text = "2"

        _xml_elem_sub4.children.append(_xml_elem_sub_sub1)
        _xml_elem_sub4.children.append(_xml_elem_sub_sub2)

        _xml_resource.children.append(_xml_elem_sub1)
        _xml_resource.children.append(_xml_elem_sub2)
        _xml_resource.children.append(_xml_elem_sub3)
        _xml_resource.children.append(_xml_elem_sub4)

        _xml_resource.lst.append(_xml_elem_sub4)

        _xml_root.lst.append(_xml_resource)

        _client = MagicMock(spec="iris_sdk.client.Client")

        _baz = Baz(_client, "foo")
        _baz._from_xml(element=_xml_root)

        #self.assertEqual(camel_patched.call_args_list,
        #    [call("Baz"), call("Fred")])
        #self.assertEqual(under_patched.call_args_list,
        #    [call("QuxQuux"), call("GarplyWaldo"), call("JimSheila"),
        #     call("Fred"), call("Barney"), call("Barney")])
        #self.assertEqual(_xml_root._call_arg, "Baz")

        _baz._from_xml(element=_xml_root)
        #self.assertEqual(_xml_root._call_arg, "Spam")

if __name__ == "__main__":
    main()