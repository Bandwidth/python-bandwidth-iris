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

XML_RESPONSE_ACCOUNT_GET = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b" <AccountResponse>"
    b"    <Account>"
    b"        <AccountId>123456</AccountId>"
    b"        <CompanyName>Spam</CompanyName>"
    b"        <AccountType>Ham</AccountType>"
    b"        <Tiers>"
    b"            <Tier>0</Tier>"
    b"        </Tiers>"
    b"        <Address>"
    b"            <HouseNumber>900</HouseNumber>"
    b"        </Address>"
    b"    </Account>"
    b"</AccountResponse>"
)

class ClassAccountGetTest(TestCase):

    """Test account mapping"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._client
        del cls._account

    def test_account_get(self):
        self.assertEquals(self._account.id, "bar")
        self.assertEquals(self._account.get_xpath(), "/accounts/bar")
        with requests_mock.Mocker() as m:
            m.get("http://foo/accounts/bar", content=XML_RESPONSE_ACCOUNT_GET)
            self._account.get()
            self.assertEquals(self._account.id, "123456")
            self.assertEquals(self._account.company_name, "Spam")
            self.assertEquals(self._account.account_type, "Ham")
            self.assertEquals(self._account.tiers.tier.items, ["0"])
            self.assertEquals(self._account.address.house_number, "900")

if __name__ == "__main__":
    main()