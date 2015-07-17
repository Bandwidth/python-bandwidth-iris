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

class ClassSubscriptionsTest(TestCase):

    """Notification subscriptions tests"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._client
        del cls._account

    def test_subscriptions_create(self):

        subscription = self._account.subscriptions.create({
            "order_type": "portins",
            "order_id": "98939562-90b0-40e9-8335-5526432d9741",
            "email_subscription": {
                "email": "foo@bar.baz",
                "digest_requested": "DAILY"
            }
        }, False)

        self.assertEqual(subscription.order_type, "portins")
        self.assertEqual(subscription.order_id,
            "98939562-90b0-40e9-8335-5526432d9741")
        self.assertEqual(subscription.email_subscription.email, "foo@bar.baz")
        self.assertEqual(subscription.email_subscription.digest_requested,
            "DAILY")

        with requests_mock.Mocker() as m:

            url = self._client.config.url + \
                self._account.subscriptions.get_xpath()
            m.post(url, headers={"location": ".../777"})

            subscription.save()

            self.assertEqual(subscription.id, "777")

if __name__ == "__main__":
    main()