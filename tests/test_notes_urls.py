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
from iris_sdk.models.portout import PortOut

class ClassNotesUrlsTest(TestCase):

    """Test the Notes resource URI linking"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._client
        del cls._account

    def test_notes_disconnects(self):
        with requests_mock.Mocker() as m:
            disc = self._account.disconnects.create({"order_id": "1"}, False)
            m.get(self._client.config.url + disc.notes.get_xpath())
            disc.notes.list()

    def test_notes_orders(self):
        with requests_mock.Mocker() as m:
            ord = self._account.orders.create({"order_id": "2"}, False)
            m.get(self._client.config.url + ord.notes.get_xpath())
            ord.notes.list()

    def test_notes_portins(self):
        with requests_mock.Mocker() as m:
            pin = self._account.portins.create({"order_id": "3"}, False)
            m.get(self._client.config.url + pin.notes.get_xpath())
            pin.notes.list()

    def test_notes_portouts(self):
        with requests_mock.Mocker() as m:
            po = PortOut(self._account.portouts)
            po.id = "4"
            m.get(self._client.config.url + po.notes.get_xpath())
            po.notes.list()

if __name__ == "__main__":
    main()