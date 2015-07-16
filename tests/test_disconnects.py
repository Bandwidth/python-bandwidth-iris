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
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<DisconnectTelephoneNumberOrderResponse>    <ErrorList>        "
    "<Error>            <Code>5006</Code>            "
    "<Description>Telephone number could not be disconnected since it is \
    not associated with your account</Description>            "
    "<TelephoneNumber>9192755703</TelephoneNumber>        </Error>        "
    "<Error>            <Code>5006</Code>            "
    "<Description>Telephone number could not be disconnected since it is \
    not associated with your account</Description>            "
    "<TelephoneNumber>9192755378</TelephoneNumber>        </Error>    "
    "</ErrorList>    <orderRequest>        "
    "<CustomerOrderId>Disconnect1234</CustomerOrderId>        "
    "<OrderCreateDate>2015-06-17T18:14:08.683Z</OrderCreateDate>        "
    "<id>b902dee1-0585-4258-becd-5c7e51ccf5e1</id>        "
    "<DisconnectTelephoneNumberOrderType>            "
    "<TelephoneNumberList>                "
    "<TelephoneNumber>9192755378</TelephoneNumber>                "
    "<TelephoneNumber>9192755703</TelephoneNumber>            "
    "</TelephoneNumberList>            "
    "<DisconnectMode>normal</DisconnectMode>        "
    "</DisconnectTelephoneNumberOrderType>    </orderRequest>    "
    "<OrderStatus>FAILED</OrderStatus>"
    "</DisconnectTelephoneNumberOrderResponse>"
)

XML_RESPONSE_DISCONNECT_POST = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<DisconnectTelephoneNumberOrderResponse> <orderRequest>  "
    "<CustomerOrderId>Disconnect1234</CustomerOrderId>  "
    "<OrderCreateDate>2015-06-17T18:14:08.683Z</OrderCreateDate>  "
    "<id>b902dee1-0585-4258-becd-5c7e51ccf5e1</id>  "
    "<DisconnectTelephoneNumberOrderType>   <TelephoneNumberList>    "
    "<TelephoneNumber>9192755378</TelephoneNumber>    "
    "<TelephoneNumber>9192755703</TelephoneNumber>   "
    "</TelephoneNumberList>   <DisconnectMode>normal</DisconnectMode>  "
    "</DisconnectTelephoneNumberOrderType> </orderRequest> "
    "<OrderStatus>RECEIVED</OrderStatus>"
    "</DisconnectTelephoneNumberOrderResponse>"
)

XML_RESPONSE_DISCONNECTS_LIST = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<ResponseSelectWrapper><ListOrderIdUserIdDate><TotalCount>7</TotalCount>"
    "<Links></Links><OrderIdUserIdDate><CountOfTNs>1</CountOfTNs>"
    "<userId>smckinnon</userId>"
    "<lastModifiedDate>2014-01-10T17-34-15Z</lastModifiedDate>"
    "<OrderId>6d7da966-e071-4741-b31c-1d8932f4b8da</OrderId>"
    "<OrderType>disconnect</OrderType>"
    "<OrderDate>2014-01-10T17-34-15.797Z</OrderDate>"
    "<OrderStatus>COMPLETE</OrderStatus><TelephoneNumberDetails>"
    "</TelephoneNumberDetails></OrderIdUserIdDate><OrderIdUserIdDate>"
    "<CountOfTNs>1</CountOfTNs><userId>jbm</userId>"
    "<lastModifiedDate>2013-12-04T21-59-32Z</lastModifiedDate>"
    "<OrderId>4ffe9262-1965-4479-a1d5-b8584440667d</OrderId>"
    "<OrderType>disconnect</OrderType>"
    "<OrderDate>2013-12-04T21-59-32.243Z</OrderDate>"
    "<OrderStatus>COMPLETE</OrderStatus><TelephoneNumberDetails>"
    "</TelephoneNumberDetails></OrderIdUserIdDate></ListOrderIdUserIdDate>"
    "</ResponseSelectWrapper>"
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

    def test_disconnect_create(self):
        self.assertEquals(self._account.disconnects.get_xpath(),
            self._account.get_xpath() + self._account.disconnects._xpath)
        url = self._client.config.url + self._account.disconnects.get_xpath()
        with requests_mock.Mocker() as m:
            m.post(url, content=XML_RESPONSE_DISCONNECT_POST)
            disconnect = self._account.disconnects.create({
                "name": "test disconnect order 4",
                "customer_order_id": "Disconnect1234",
                "disconnect_telephone_number_order_type": {
                    "telephone_number_list": {
                        "telephone_number": ["9192755378", "9192755703"]
                    }
                }
            })
            self.assertEquals(m.request_history[0].method, "POST")
            self.assertEquals(disconnect.id,
                "b902dee1-0585-4258-becd-5c7e51ccf5e1")
            self.assertEquals(disconnect.order_id, disconnect.id)
            self.assertEquals(disconnect.customer_order_id, "Disconnect1234")
            self.assertEquals(disconnect.order_create_date,
                "2015-06-17T18:14:08.683Z")
            order_type = disconnect.disconnect_telephone_number_order_type
            self.assertEquals(
                order_type.telephone_number_list.telephone_number.items,
                ["9192755378", "9192755703"])
            self.assertEquals(order_type.disconnect_mode, "normal")
            self.assertEquals(disconnect.order_status, "RECEIVED")

    def test_disconnect_get(self):
        disconnect = self._account.disconnects.create({"order_id":
            "b902dee1-0585-4258-becd-5c7e51ccf5e1"}, False)
        self.assertEquals(disconnect.get_xpath(),
            self._account.get_xpath() + self._account.disconnects._xpath +
                disconnect._xpath.format(disconnect.id))
        url = self._client.config.url + disconnect.get_xpath()
        with requests_mock.Mocker() as m:
            m.get(url, content=XML_RESPONSE_DISCONNECT_GET)
            resp = disconnect.get({"tndetail": "true"})
            req = resp.order_request
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(req.id, "b902dee1-0585-4258-becd-5c7e51ccf5e1")
            self.assertEquals(req.customer_order_id, "Disconnect1234")
            order_type = req.disconnect_telephone_number_order_type
            self.assertEquals(
                order_type.telephone_number_list.telephone_number.items,
                ["9192755378","9192755703"])
            self.assertEquals(order_type.disconnect_mode, "normal")
            self.assertEquals(req.order_create_date,
                "2015-06-17T18:14:08.683Z")

            error = resp.error_list.error.items[0]
            self.assertEquals(error.code, "5006")
            self.assertEquals(error.telephone_number, "9192755703")
            self.assertTrue(error.description.startswith(
                "Telephone number could not be disconnected"))
            error = resp.error_list.error.items[1]
            self.assertEquals(error.code, "5006")
            self.assertEquals(error.telephone_number, "9192755378")
            self.assertTrue(error.description.startswith(
               "Telephone number could not be disconnected"))

    def test_disconnects_get(self):
        self.assertEquals(self._account.disconnects.get_xpath(),
            self._account.get_xpath() + self._account.disconnects._xpath)
        url = self._client.config.url + self._account.disconnects.get_xpath()
        with requests_mock.Mocker() as m:
            m.get(url, content=XML_RESPONSE_DISCONNECTS_LIST)
            disconnects = self._account.disconnects.list({"page":1,"size":5})
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(len(disconnects.items), 2)
            disc = disconnects.items[0]
            self.assertEquals(disc.count_of_tns, "1")
            self.assertEquals(disc.user_id, "smckinnon")
            self.assertEquals(disc.last_modified_date, "2014-01-10T17-34-15Z")
            self.assertEquals(disc.order_id,
                "6d7da966-e071-4741-b31c-1d8932f4b8da")
            self.assertEquals(disc.order_type, "disconnect")
            self.assertEquals(disc.order_date, "2014-01-10T17-34-15.797Z")
            self.assertEquals(disc.order_status, "COMPLETE")

if __name__ == "__main__":
    main()