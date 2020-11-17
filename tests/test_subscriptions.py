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

XML_RESPONSE_SUBSCRIPTIONS_LIST = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<SubscriptionsResponse><Subscriptions><Subscription>"
    b"<SubscriptionId>1</SubscriptionId><OrderType>orders</OrderType>"
    b"<OrderId>8684b1c8-7d41-4877-bfc2-6bd8ea4dc89f</OrderId>"
    b"<EmailSubscription><Email>test@test</Email>"
    b"<DigestRequested>NONE</DigestRequested></EmailSubscription>"
    b"</Subscription></Subscriptions></SubscriptionsResponse>"
)

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

    def test_subscriptions_create_for_orders(self):

        subscription = self._account.subscriptions.create({
            "order_type": "orders",
            "callback_subscription": {
                "url": "https://someurl",
                "expiry": "86400",
            }
        }, False)

        self.assertEqual(subscription.order_type, "orders")
        self.assertEqual(subscription.callback_subscription.url, "https://someurl")
        self.assertEqual(subscription.callback_subscription.expiry, '86400')

        with requests_mock.Mocker() as m:

            url = self._client.config.url + \
                self._account.subscriptions.get_xpath()
            m.post(url, headers={"location": ".../777"})

            subscription.save()

            self.assertEqual(subscription.id, "777")

    def test_subscriptions_list(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + \
                self._account.subscriptions.get_xpath()
            m.get(url, content=XML_RESPONSE_SUBSCRIPTIONS_LIST)

            subs = self._account.subscriptions.list({"orderType": "portins"})
            sub = subs.items[0]

            self.assertEqual(len(subs.items), 1)
            self.assertEqual(sub.order_id,
                "8684b1c8-7d41-4877-bfc2-6bd8ea4dc89f")

    def test_subscriptions_update(self):

        subscription = self._account.subscriptions.create({
            "subscription_id": "1c59e661-8c90-4cb5-aab1-00547ea45ecb",
            "order_type": "portins",
            "order_id": "98939562-90b0-40e9-8335-5526432d9741",
            "email_subscription": {
                "email": "foo@bar.baz",
                "digest_requested": "DAILY"
            }
        }, False);

        self.assertEqual(subscription.subscription_id,
            "1c59e661-8c90-4cb5-aab1-00547ea45ecb")
        self.assertEqual(subscription.order_type, "portins")
        self.assertEqual(subscription.order_id,
            "98939562-90b0-40e9-8335-5526432d9741")

        with requests_mock.Mocker() as m:
            url = self._client.config.url + subscription.get_xpath()
            m.put(requests_mock.ANY)
            subscription.save()

            self.assertEqual(m.request_history[0].url, url)

    def test_subscriptions_delete(self):

        subscription = self._account.subscriptions.create(
            {"subscription_id": "1c59e661"}, False);

        with requests_mock.Mocker() as m:
            url = self._client.config.url + subscription.get_xpath()
            m.delete(requests_mock.ANY)
            subscription.delete()

            self.assertEqual(m.request_history[0].url, url)

if __name__ == "__main__":
    main()