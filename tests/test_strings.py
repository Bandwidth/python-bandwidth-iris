#!/usr/bin/env python

import os
import sys

# For coverage.
if __package__ is None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from unittest import main, TestCase

from iris_sdk.utils.strings import Converter

class ClassStringsConverterTest(TestCase):

    """Test HTTP requests."""

    @classmethod
    def setUp(cls):
        cls._converter = Converter()

    @classmethod
    def tearDown(cls):
        del cls._converter

    def test_to_camelcase(self):
        tests = [
            ('foo_bar', 'FooBar'),
            ('FooBar', 'FooBar'),
            ('_foo_bar', 'FooBar'),
            ('_foo__bar', 'Foo_Bar')]

        for input, output in tests:
            self.assertEqual(self._converter.to_camelcase(input), output)

    def test_to_underscore(self):
        tests = [
            ('foobar', 'foobar'),
            ('foo_bar', 'foo_bar'),
            ('FooBar', 'foo_bar'),
            ('_foo__bar', '_foo__bar')]

        for input, output in tests:
            self.assertEqual(self._converter.to_underscore(input), output)

if __name__ == "__main__":
    main()