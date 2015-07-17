#!/usr/bin/env python

import os
import sys

# For coverage.
if __package__ is None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from unittest import main, TestCase

import requests
import requests_mock

from iris_sdk.client import Client
from iris_sdk.models.account import Account

XML_RESPONSE_NOTES_GET = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><Notes>"
    "<Note><Id>11425</Id><UserId>byo_dev</UserId>"
    "<Description>Test Note</Description>"
    "<LastDateModifier>2015-06-18T04:19:59.000Z</LastDateModifier></Note>"
    "</Notes>"
)

XML_RESPONSE_NOTES_LIST = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><Notes>"
    "<Note><Id>11425</Id><UserId>byo_dev</UserId>"
    "<Description>Test Note</Description>"
    "<LastDateModifier>2015-06-18T04:19:59.000Z</LastDateModifier></Note>"
    "<Note><Id>11425</Id><UserId>byo_dev</UserId>"
    "<Description>Test Note</Description>"
    "<LastDateModifier>2015-06-18T04:19:59.000Z</LastDateModifier></Note>"
    "</Notes>"
)

class ClassNotesTest(TestCase):

    """Test the Notes resource"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)
        cls._notes = cls._account.disconnects.create(
            {"order_id": "123"}, False).notes
        cls._url = cls._client.config.url + cls._notes.get_xpath()

    @classmethod
    def tearDownClass(cls):
        del cls._notes
        del cls._account
        del cls._client

    def test_notes_create(self):
        with requests_mock.Mocker() as m:
            m.post(self._url, headers={"location": self._url + "/123"})
            note = self._notes.create({"user_id":"spam", "description":"ham"})
            self.assertEqual(note.id, "123")

    def test_notes_get(self):
        with requests_mock.Mocker() as m:
            m.get(self._url, content=XML_RESPONSE_NOTES_GET)
            notes = self._notes.list()
            self.assertEqual(notes.items[0].id, "11425")

    def test_notes_list(self):
        with requests_mock.Mocker() as m:
            m.get(self._url, content=XML_RESPONSE_NOTES_LIST)
            notes = self._notes.list()
            self.assertEqual(len(notes.items), 2)
            self.assertEqual(notes.items[0].id, "11425")

if __name__ == "__main__":
    main()