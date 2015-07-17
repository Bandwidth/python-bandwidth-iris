#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

import os
import sys

# For coverage.
if __package__ is None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from iris_sdk.utils.py_compat import PY_VER_MAJOR

from unittest import main, TestCase

if PY_VER_MAJOR == 3:
    from unittest.mock import call, MagicMock, patch
else:
    from mock import call, MagicMock, patch

from xml.etree.ElementTree import Element, ElementTree, fromstring

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.maps.base_map import BaseMap

class FooMap(BaseMap):
    fred = "A"
    barney = "B"
    qux_quux = "R"
    bar = None

class BarMap(BaseMap):
    spam = 1
    ham = 2
    eggs = 3

class Foo(BaseResource, FooMap):
    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        self.bar = Bar()

class Bar(BaseResource, BarMap):
    pass

class ClassBaseResourceInitTest(TestCase):

    """Test class initialization and properties"""

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

        foo = MagicMock(BaseResource)
        self._base_resource = BaseResource(foo)
        self.assertEqual(self._base_resource._client, foo.client)

class ClassBaseResourceXmlTest(TestCase):

    """Test XML conversion"""

    def setUp(self):
        self.foo = Foo()
        self.str = ("<?xml version='1.0' encoding='UTF-8'?>\n"
            "<Foo><Bar><Eggs>3</Eggs><Ham>2</Ham><Spam>1</Spam></Bar>"
            "<Barney>B</Barney><Fred>A</Fred><QuxQuux>R</QuxQuux></Foo>")

    def test_baseresource_from_xml(self):

        root = self.foo._element_from_string(self.str)
        self.foo.clear()
        self.assertIsNone(self.foo.fred)
        self.foo._from_xml(root)

        self.assertEqual(self.foo.barney, "B")
        self.assertEqual(self.foo.fred, "A")
        self.assertEqual(self.foo.qux_quux, "R")

    def test_baseresource_to_xml(self):

        xml = self.foo._serialize()

        self.assertEqual(self.str, xml)

if __name__ == "__main__":
    main()