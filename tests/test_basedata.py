#!/usr/bin/env python

import os
import sys

# For coverage.
if __package__ is None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from unittest import main, TestCase

from iris_sdk.models.base_resource import BaseData

class BaseDataStub(BaseData):
    foo = 1

class BaseDataStubDescendant(BaseDataStub):
    spam = "ham"

class TestStub(BaseDataStub):
    _baz = 3
    bar = 2
    client = 4
    eggs = None
    fred = None
    items = 5
    xpath = 6
    def __init__(self):
        self.eggs = BaseDataStubDescendant()
        self.fred = BaseData()
        self.fred.barney = 7

class ClassBaseDataClearTest(TestCase):

    """Test BaseData's clear method"""

    def setUp(self):
        self._test_stub = TestStub()

    def tearDown(self):
        del self._test_stub

    def test_basedata_clear(self):

        self._test_stub.clear()

        self.assertEqual(self._test_stub._baz, 3)
        self.assertEqual(self._test_stub.bar, None)
        self.assertEqual(self._test_stub.client, 4)
        self.assertEqual(self._test_stub.eggs.spam, None)
        self.assertEqual(self._test_stub.foo, None)
        self.assertEqual(self._test_stub.fred.barney, None)
        self.assertEqual(self._test_stub.items, 5)
        self.assertEqual(self._test_stub.xpath, 6)

class ClassBaseDataDictTest(TestCase):

    """Test BaseData's dict initialization"""

    def setUp(self):
        self._test_stub = TestStub()

    def tearDown(self):
        del self._test_stub

    def test_basedata_clear(self):

        self._test_stub.set_from_dict({
            "_baz": "34", "bar": "2",
            "eggs": {
                "spam": "foo"
            }
        })

        self.assertEqual(self._test_stub._baz, "34")
        self.assertEqual(self._test_stub.bar, "2")
        self.assertEqual(self._test_stub.eggs.spam, "foo")

if __name__ == "__main__":
    main()