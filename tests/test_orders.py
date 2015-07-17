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

XML_RESPONSE_ORDER_CREATE = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<OrderResponse><Order><CustomerOrderId>123456789</CustomerOrderId>"
    "<Name>Available Telephone Number order</Name>"
    "<OrderCreateDate>2015-06-20T10:54:08.042Z</OrderCreateDate>"
    "<BackOrderRequested>false</BackOrderRequested>"
    "<id>f30a31a1-1de4-4939-b094-4521bbe5c8df</id>"
    "<ExistingTelephoneNumberOrderType><TelephoneNumberList>"
    "<TelephoneNumber>9193752369</TelephoneNumber>"
    "<TelephoneNumber>9193752720</TelephoneNumber></TelephoneNumberList>"
    "</ExistingTelephoneNumberOrderType><PartialAllowed>true</PartialAllowed>"
    "<SiteId>2297</SiteId></Order><OrderStatus>RECEIVED</OrderStatus>"
    "</OrderResponse>"
)

XML_RESPONSE_ORDER_GET = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<OrderResponse><Order><CustomerOrderId>123456789</CustomerOrderId>"
    "<Name>Available Telephone Number order</Name>"
    "<OrderCreateDate>2015-06-20T10:54:08.042Z</OrderCreateDate>"
    "<BackOrderRequested>false</BackOrderRequested>"
    "<id>f30a31a1-1de4-4939-b094-4521bbe5c8df</id>"
    "<ExistingTelephoneNumberOrderType><TelephoneNumberList>"
    "<TelephoneNumber>9193752369</TelephoneNumber>"
    "<TelephoneNumber>9193752720</TelephoneNumber>"
    "<TelephoneNumber>9193752648</TelephoneNumber>"
    "</TelephoneNumberList></ExistingTelephoneNumberOrderType>"
    "<PartialAllowed>true</PartialAllowed><SiteId>2297</SiteId></Order>"
    "<OrderStatus>RECEIVED</OrderStatus></OrderResponse>"
)

XML_RESPONSE_ORDERS_LIST = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><"
    "ResponseSelectWrapper><ListOrderIdUserIdDate><TotalCount>2</TotalCount>"
    "<Links><first></first></Links><OrderIdUserIdDate>"
    "<CountOfTNs>0</CountOfTNs><CustomerOrderId>123456789</CustomerOrderId>"
    "<userId>byo_dev</userId>"
    "<lastModifiedDate>2015-06-13T16:14:46.017Z</lastModifiedDate>"
    "<OrderDate>2015-06-13T16:14:45.956Z</OrderDate>"
    "<OrderType>new_number</OrderType>"
    "<orderId>016c1aef-a873-4a90-8374-60771cba9452</orderId>"
    "<OrderStatus>FAILED</OrderStatus></OrderIdUserIdDate><OrderIdUserIdDate>"
    "<CountOfTNs>0</CountOfTNs><CustomerOrderId>123456789</CustomerOrderId>"
    "<userId>byo_dev</userId>"
    "<lastModifiedDate>2015-06-13T16:32:04.216Z</lastModifiedDate>"
    "<OrderDate>2015-06-13T16:32:04.181Z</OrderDate>"
    "<OrderType>new_number</OrderType>"
    "<orderId>77659f47-d527-42ad-bf72-34b6841016ac</orderId>"
    "<OrderStatus>FAILED</OrderStatus></OrderIdUserIdDate>"
    "</ListOrderIdUserIdDate></ResponseSelectWrapper>"
)

class ClassOrdersTest(TestCase):

    """Test phone number orders"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._client
        del cls._account

    def test_area_search_and_order(self):

        order = self._account.orders.create({
            "name": "Available telephone number order",
            "site_id": "2297",
            "customer_order_id": "123456789",
            "area_code_search_and_order_type": {
                "area_code": "617",
                "quantity": "1"
            }
        }, False)

        self.assertEqual(order.name, "Available telephone number order")
        self.assertEqual(order.site_id, "2297")
        self.assertEqual(order.customer_order_id, "123456789")
        self.assertEqual(order.area_code_search_and_order_type.area_code,
            "617")
        self.assertEqual(order.area_code_search_and_order_type.quantity,
            "1")

    def test_city_search_and_order(self):

        order = self._account.orders.create({
            "name": "Available telephone number order",
            "site_id": "2297",
            "customer_order_id": "123456789",
            "city_search_and_order_type": {
                "state": "NC",
                "city": "RALEIGH",
                "quantity": "1"
            }
        }, False)

        self.assertEqual(order.name, "Available telephone number order")
        self.assertEqual(order.site_id, "2297")
        self.assertEqual(order.customer_order_id, "123456789")
        self.assertEqual(order.city_search_and_order_type.state, "NC")
        self.assertEqual(order.city_search_and_order_type.city, "RALEIGH")
        self.assertEqual(order.city_search_and_order_type.quantity, "1")

    def test_lata_search_and_order(self):

        order = self._account.orders.create({
            "name": "Available telephone number order",
            "site_id": "2297",
            "customer_order_id": "123456789",
            "lata_search_and_order_type": {
                "lata": "224",
                "quantity": "1"
            }
        }, False)

        self.assertEqual(order.name, "Available telephone number order")
        self.assertEqual(order.site_id, "2297")
        self.assertEqual(order.customer_order_id, "123456789")
        self.assertEqual(order.lata_search_and_order_type.lata, "224")
        self.assertEqual(order.lata_search_and_order_type.quantity, "1")

    def test_npa_search_and_order(self):

        order = self._account.orders.create({
            "name": "Available telephone number order",
            "site_id": "2297",
            "customer_order_id": "123456789",
            "npanxx_search_and_order_type": {
                "npa_nxx": "919439",
                "quantity": "1"
            }
        }, False)

        self.assertEqual(order.name, "Available telephone number order")
        self.assertEqual(order.site_id, "2297")
        self.assertEqual(order.customer_order_id, "123456789")
        self.assertEqual(order.npanxx_search_and_order_type.npa_nxx, "919439")
        self.assertEqual(order.npanxx_search_and_order_type.quantity, "1")

    def test_order_create(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._account.orders.get_xpath()
            m.post(url, content=XML_RESPONSE_ORDER_CREATE)

            order = self._account.orders.create({
                "name": "Available telephone number order",
                "site_id": "2297",
                "customer_order_id": "123456789",
                "existing_telephone_number_order_type": {
                    "telephone_number_list": {
                        "telephone_number": ["9193752369", "9193752720"]
                    }
                }
            })

            self.assertEqual(order.id, "f30a31a1-1de4-4939-b094-4521bbe5c8df")
            self.assertEqual(order.order_status, "RECEIVED")

    def test_order_get(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._account.orders.get_xpath()+\
                "/f30a31a1-1de4-4939-b094-4521bbe5c8df"
            m.get(url, content=XML_RESPONSE_ORDER_GET)

            order = self._account.orders.get(
                "f30a31a1-1de4-4939-b094-4521bbe5c8df")

            self.assertEqual(order.id,
                "f30a31a1-1de4-4939-b094-4521bbe5c8df")
            self.assertEqual(order.order_status, "RECEIVED")

    def test_order_update(self):

        with requests_mock.Mocker() as m:

            order = self._account.orders.create({
                "id": "f30a31a1-1de4-4939-b094-4521bbe5c8df",
                "name": "Available telephone number order",
                "customer_order_id": "123456789",
                "close_order": "true"
            }, False)

            url = self._client.config.url + order.get_xpath()
            m.put(url, content=XML_RESPONSE_ORDER_CREATE)

            self.assertEqual(order.close_order, "true")

    def test_orders_list(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._account.orders.get_xpath()
            m.get(url, content=XML_RESPONSE_ORDERS_LIST)

            ord = self._account.orders.list({"page": 1, "size": 20})

            self.assertEqual(len(ord.items), 2)
            self.assertEqual(ord.items[0].id,
                "016c1aef-a873-4a90-8374-60771cba9452")
            self.assertEqual(ord.items[0].customer_order_id, "123456789")
            self.assertEqual(ord.items[0].order_type, "new_number")
            self.assertEqual(ord.items[0].count_of_tns, "0")
            self.assertEqual(ord.items[0].order_status, "FAILED")

    def test_rate_center_search_and_order(self):

        order = self._account.orders.create({
            "name": "Available telephone number order",
            "site_id": "2297",
            "customer_order_id": "123456789",
            "rate_center_search_and_order_type": {
                "rate_center": "RALEIGH",
                "state": "NC",
                "quantity": "1"
            }
        }, False)

        self.assertEqual(order.name, "Available telephone number order")
        self.assertEqual(order.site_id, "2297")
        self.assertEqual(order.customer_order_id, "123456789")
        self.assertEqual(order.rate_center_search_and_order_type.rate_center,
            "RALEIGH")
        self.assertEqual(order.rate_center_search_and_order_type.state, "NC")
        self.assertEqual(order.rate_center_search_and_order_type.quantity,"1")

    def test_state_search_and_order(self):

        order = self._account.orders.create({
            "name": "Available telephone number order",
            "site_id": "2297",
            "customer_order_id": "123456789",
            "state_search_and_order_type": {
                "state": "NC",
                "quantity": "1"
            }
        }, False)

        self.assertEqual(order.name, "Available telephone number order")
        self.assertEqual(order.site_id, "2297")
        self.assertEqual(order.customer_order_id, "123456789")
        self.assertEqual(order.state_search_and_order_type.state, "NC")
        self.assertEqual(order.state_search_and_order_type.quantity,"1")

    def test_toll_free_vanity_search_and_order(self):

        order = self._account.orders.create({
            "name": "Available telephone number order",
            "site_id": "2297",
            "customer_order_id": "123456789",
            "toll_free_vanity_search_and_order_type": {
                "toll_free_vanity": "newcars",
                "quantity": "1"
            }
        }, False)

        self.assertEqual(order.name, "Available telephone number order")
        self.assertEqual(order.site_id, "2297")
        self.assertEqual(order.customer_order_id, "123456789")
        self.assertEqual(order.toll_free_vanity_search_and_order_type.\
            toll_free_vanity, "newcars")
        self.assertEqual(order.toll_free_vanity_search_and_order_type.\
            quantity,"1")

    def test_toll_free_wildcard_search_and_order(self):

        order = self._account.orders.create({
            "name": "Available telephone number order",
            "site_id": "2297",
            "customer_order_id": "123456789",
            "toll_free_wild_char_search_and_order_type": {
                "toll_free_wild_card_pattern": "8**",
                "quantity": "1"
            }
        }, False)

        self.assertEqual(order.name, "Available telephone number order")
        self.assertEqual(order.site_id, "2297")
        self.assertEqual(order.customer_order_id, "123456789")
        self.assertEqual(order.toll_free_wild_char_search_and_order_type.\
            toll_free_wild_card_pattern, "8**")
        self.assertEqual(order.toll_free_wild_char_search_and_order_type.\
            quantity,"1")

    def test_zip_search_and_order(self):

        order = self._account.orders.create({
            "name": "Available telephone number order",
            "site_id": "2297",
            "customer_order_id": "123456789",
            "zip_search_and_order_type": {
                "zip": "1337",
                "quantity": "1"
            }
        }, False)

        self.assertEqual(order.name, "Available telephone number order")
        self.assertEqual(order.site_id, "2297")
        self.assertEqual(order.customer_order_id, "123456789")
        self.assertEqual(order.zip_search_and_order_type.zip, "1337")
        self.assertEqual(order.zip_search_and_order_type.quantity,"1")

if __name__ == "__main__":
    main()