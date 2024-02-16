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

XML_RESPONSE_DISCONNECT_GET = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<DisconnectTelephoneNumberOrderResponse><ErrorList>"
    b"<Error><Code>5006</Code>"
    b"<Description>Telephone number could not be disconnected since it is \
    bnot associated with your account</Description>"
    b"<TelephoneNumber>9192755703</TelephoneNumber></Error>"
    b"<Error><Code>5006</Code>"
    b"<Description>Telephone number could not be disconnected since it is \
    not associated with your account</Description>"
    b"<TelephoneNumber>9192755378</TelephoneNumber></Error>"
    b"</ErrorList><orderRequest>"
    b"<CustomerOrderId>Disconnect1234</CustomerOrderId>"
    b"<OrderCreateDate>2015-06-17T18:14:08.683Z</OrderCreateDate>"
    b"<id>b902dee1-0585-4258-becd-5c7e51ccf5e1</id>"
    b"<DisconnectTelephoneNumberOrderType>"
    b"<TelephoneNumberList>"
    b"<TelephoneNumber>9192755378</TelephoneNumber>"
    b"<TelephoneNumber>9192755703</TelephoneNumber>"
    b"</TelephoneNumberList>"
    b"<DisconnectMode>normal</DisconnectMode>"
    b"</DisconnectTelephoneNumberOrderType></orderRequest>"
    b"<OrderStatus>FAILED</OrderStatus>"
    b"</DisconnectTelephoneNumberOrderResponse>"
)

XML_RESPONSE_DISCONNECT_POST = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<DisconnectTelephoneNumberOrderResponse><orderRequest>"
    b"<CustomerOrderId>Disconnect1234</CustomerOrderId>"
    b"<OrderCreateDate>2015-06-17T18:14:08.683Z</OrderCreateDate>"
    b"<id>b902dee1-0585-4258-becd-5c7e51ccf5e1</id>"
    b"<DisconnectTelephoneNumberOrderType><TelephoneNumberList>"
    b"<TelephoneNumber>9192755378</TelephoneNumber>"
    b"<TelephoneNumber>9192755703</TelephoneNumber>"
    b"</TelephoneNumberList><DisconnectMode>normal</DisconnectMode>"
    b"</DisconnectTelephoneNumberOrderType></orderRequest>"
    b"<OrderStatus>RECEIVED</OrderStatus>"
    b"</DisconnectTelephoneNumberOrderResponse>"
)

XML_RESPONSE_DISCONNECTS_LIST = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<ResponseSelectWrapper><ListOrderIdUserIdDate><TotalCount>7</TotalCount>"
    b"<Links></Links><OrderIdUserIdDate><CountOfTNs>1</CountOfTNs>"
    b"<userId>smckinnon</userId>"
    b"<lastModifiedDate>2014-01-10T17-34-15Z</lastModifiedDate>"
    b"<OrderId>6d7da966-e071-4741-b31c-1d8932f4b8da</OrderId>"
    b"<OrderType>disconnect</OrderType>"
    b"<OrderDate>2014-01-10T17-34-15.797Z</OrderDate>"
    b"<OrderStatus>COMPLETE</OrderStatus><TelephoneNumberDetails>"
    b"</TelephoneNumberDetails></OrderIdUserIdDate><OrderIdUserIdDate>"
    b"<CountOfTNs>1</CountOfTNs><userId>jbm</userId>"
    b"<lastModifiedDate>2013-12-04T21-59-32Z</lastModifiedDate>"
    b"<OrderId>4ffe9262-1965-4479-a1d5-b8584440667d</OrderId>"
    b"<OrderType>disconnect</OrderType>"
    b"<OrderDate>2013-12-04T21-59-32.243Z</OrderDate>"
    b"<OrderStatus>COMPLETE</OrderStatus><TelephoneNumberDetails>"
    b"</TelephoneNumberDetails></OrderIdUserIdDate></ListOrderIdUserIdDate>"
    b"</ResponseSelectWrapper>"
)

class ClassDisconnectsTest(TestCase):

    """Test phone disconnect orders"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._client
        del cls._account

    # def test_disconnect_create(self):

        # with requests_mock.Mocker() as m:

            # url =self._client.config.url+self._account.disconnects.get_xpath()
            # m.post(url, content=XML_RESPONSE_DISCONNECT_POST)

            # disconnect = self._account.disconnects.create({
            #     "name": "test disconnect order 4",
            #     "customer_order_id": "Disconnect1234",
            #     "disconnect_telephone_number_order_type": {
            #         "telephone_number_list": {
            #             "telephone_number": ["9192755378", "9192755703"]
            #         }
            #     }
            # })

            # self.assertEqual(disconnect.id,
            #     "b902dee1-0585-4258-becd-5c7e51ccf5e1")
            # self.assertEqual(disconnect.order_id, disconnect.id)
            # self.assertEqual(disconnect.customer_order_id, "Disconnect1234")
            # self.assertEqual(disconnect.order_create_date,
            #     "2015-06-17T18:14:08.683Z")
            # order_type = disconnect.disconnect_telephone_number_order_type
            # self.assertEqual(
            #     order_type.telephone_number_list.telephone_number.items,
            #     ["9192755378", "9192755703"])
            # self.assertEqual(order_type.disconnect_mode, "normal")
            # self.assertEqual(disconnect.order_status, "RECEIVED")

    def test_disconnect_get(self):

        with requests_mock.Mocker() as m:

            url =self._client.config.url+self._account.disconnects.get_xpath()
            m.get(url, content=XML_RESPONSE_DISCONNECT_GET)

            disconnect = self._account.disconnects.create({"order_id": "b902dee1-0585-4258-becd-5c7e51ccf5e1"}, False)

            resp = disconnect.get({"tndetail": "true"})
            req = resp.order_request

            self.assertEqual(req.id, "b902dee1-0585-4258-becd-5c7e51ccf5e1")
            self.assertEqual(req.customer_order_id, "Disconnect1234")

            order_type = req.disconnect_telephone_number_order_type

            self.assertEqual(
                order_type.telephone_number_list.telephone_number.items,
                ["9192755378","9192755703"])
            self.assertEqual(order_type.disconnect_mode, "normal")
            self.assertEqual(req.order_create_date,
                "2015-06-17T18:14:08.683Z")

            error = resp.error_list.error.items[0]

            self.assertEqual(error.code, "5006")
            self.assertEqual(error.telephone_number, "9192755703")
            self.assertTrue(error.description.startswith(
                "Telephone number could not be disconnected"))

            error = resp.error_list.error.items[1]

            self.assertEqual(error.code, "5006")
            self.assertEqual(error.telephone_number, "9192755378")
            self.assertTrue(error.description.startswith(
               "Telephone number could not be disconnected"))

    def test_disconnects_get(self):

        with requests_mock.Mocker() as m:

            url =self._client.config.url+self._account.disconnects.get_xpath()
            m.get(url, content=XML_RESPONSE_DISCONNECTS_LIST)

            disconnects = self._account.disconnects.list({"page":1,"size":5})

            self.assertEqual(len(disconnects.items), 2)

            disc = disconnects.items[0]

            self.assertEqual(disc.count_of_tns, "1")
            self.assertEqual(disc.user_id, "smckinnon")
            self.assertEqual(disc.last_modified_date, "2014-01-10T17-34-15Z")
            self.assertEqual(disc.order_id,
                "6d7da966-e071-4741-b31c-1d8932f4b8da")
            self.assertEqual(disc.order_type, "disconnect")
            self.assertEqual(disc.order_date, "2014-01-10T17-34-15.797Z")
            self.assertEqual(disc.order_status, "COMPLETE")

if __name__ == "__main__":
    main()