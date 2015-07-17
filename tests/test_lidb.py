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

XML_RESPONSE_LIDB_GET = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<LidbOrder><OrderCreateDate>2015-06-21T04:52:33.191Z</OrderCreateDate>"
    b"<AccountId>9500249</AccountId><CreatedByUser>byo_dev</CreatedByUser>"
    b"<OrderId>7802373f-4f52-4387-bdd1-c5b74833d6e2</OrderId>"
    b"<LastModifiedDate>2015-06-21T04:52:33.191Z</LastModifiedDate>"
    b"<ErrorList><Error><Code>11014</Code>"
    b"<Description>Number does not belong to this account</Description>"
    b"<TelephoneNumber>4352154856</TelephoneNumber></Error><Error>"
    b"<Code>11014</Code>"
    b"<Description>Number does not belong to this account</Description>"
    b"<TelephoneNumber>4352154855</TelephoneNumber></Error></ErrorList>"
    b"<ProcessingStatus>FAILED</ProcessingStatus><LidbTnGroups><LidbTnGroup>"
    b"<TelephoneNumbers><TelephoneNumber>4352154856</TelephoneNumber>"
    b"</TelephoneNumbers><SubscriberInformation>Steve</SubscriberInformation>"
    b"<UseType>RESIDENTIAL</UseType><Visibility>PUBLIC</Visibility>"
    b"</LidbTnGroup><LidbTnGroup><TelephoneNumbers>"
    b"<TelephoneNumber>4352154855</TelephoneNumber></TelephoneNumbers>"
    b"<SubscriberInformation>Steve</SubscriberInformation>"
    b"<UseType>RESIDENTIAL</UseType><Visibility>PUBLIC</Visibility>"
    b"</LidbTnGroup></LidbTnGroups></LidbOrder>"
)

XML_RESPONSE_LIDB_LIST = (
    b"<?xml version=\"1.0\"?><ResponseSelectWrapper><ListOrderIdUserIdDate>"
    b"<TotalCount>2122</TotalCount><OrderIdUserIdDate>"
    b"<accountId>9999999</accountId><CountOfTNs>0</CountOfTNs>"
    b"<lastModifiedDate>2014-02-25T16:02:43.195Z</lastModifiedDate>"
    b"<OrderType>lidb</OrderType>"
    b"<OrderDate>2014-02-25T16:02:43.195Z</OrderDate>"
    b"<orderId>abe36738-6929-4c6f-926c-88e534e2d46f</orderId>"
    b"<OrderStatus>FAILED</OrderStatus><TelephoneNumberDetails/>"
    b"<userId>team_ua</userId></OrderIdUserIdDate><OrderIdUserIdDate>"
    b"<accountId>9999999</accountId><CountOfTNs>0</CountOfTNs>"
    b"<lastModifiedDate>2014-02-25T16:02:39.021Z</lastModifiedDate>"
    b"<OrderType>lidb</OrderType>"
    b"<OrderDate>2014-02-25T16:02:39.021Z</OrderDate>"
    b"<orderId>ba5b6297-139b-4430-aab0-9ff02c4362f4</orderId>"
    b"<OrderStatus>FAILED</OrderStatus><userId>team_ua</userId>"
    b"</OrderIdUserIdDate></ListOrderIdUserIdDate></ResponseSelectWrapper>"
)

XML_RESPONSE_LIDB_POST = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<LidbOrder><CustomerOrderId>testCustomerOrderId</CustomerOrderId>"
    b"<orderId>255bda29-fc57-44e8-a6c2-59b45388c6d0</orderId>"
    b"<OrderCreateDate>2014-05-28T14:46:21.724Z</OrderCreateDate>"
    b"<ProcessingStatus>RECEIVED</ProcessingStatus>"
    b"<CreatedByUser>jbm</CreatedByUser>"
    b"<LastModifiedDate>2014-02-20T19:33:17.600Z</LastModifiedDate>"
    b"<OrderCompleteDate>2014-02-20T19:33:17.600Z</OrderCompleteDate>"
    b"<ErrorList/><LidbTnGroups><LidbTnGroup><TelephoneNumbers>"
    b"<TelephoneNumber>4082213311</TelephoneNumber></TelephoneNumbers>"
    b"<FullNumber>8042105618</FullNumber>"
    b"<SubscriberInformation>Fred</SubscriberInformation>"
    b"<UseType>BUSINESS</UseType><Visibility>PRIVATE</Visibility>"
    b"</LidbTnGroup><LidbTnGroup><TelephoneNumbers>"
    b"<TelephoneNumber>4082212850</TelephoneNumber>"
    b"<TelephoneNumber>4082213310</TelephoneNumber></TelephoneNumbers>"
    b"<FullNumber>8042105760</FullNumber>"
    b"<SubscriberInformation>Fred</SubscriberInformation>"
    b"<UseType>RESIDENTIAL</UseType><Visibility>PUBLIC</Visibility>"
    b"</LidbTnGroup></LidbTnGroups></LidbOrder>"
)

class ClassLidbTest(TestCase):

    """Test LIDB orders"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._client
        del cls._account

    def test_lidb_get(self):

        with requests_mock.Mocker() as m:

            lidb = self._account.lidbs.create()
            lidb.id = "7802373f-4f52-4387-bdd1-c5b74833d6e2"

            url = self._client.config.url + lidb.get_xpath()
            m.get(url, content=XML_RESPONSE_LIDB_GET)

            lidb = self._account.lidbs.get(
                "7802373f-4f52-4387-bdd1-c5b74833d6e2")

            self.assertEqual(lidb.order_id,
                "7802373f-4f52-4387-bdd1-c5b74833d6e2")
            self.assertEqual(lidb.account_id, "9500249")
            self.assertEqual(lidb.last_modified_date,
                "2015-06-21T04:52:33.191Z")
            self.assertEqual(lidb.order_create_date,
                "2015-06-21T04:52:33.191Z")
            self.assertEqual(lidb.processing_status, "FAILED")
            self.assertEqual(lidb.created_by_user, "byo_dev")

            error = lidb.error_list.error.items[0]

            self.assertEqual(error.telephone_number, "4352154856")
            self.assertEqual(error.code, "11014")
            self.assertEqual(error.description,
                "Number does not belong to this account")

            error = lidb.error_list.error.items[1]

            self.assertEqual(error.telephone_number, "4352154855")
            self.assertEqual(error.code, "11014")
            self.assertEqual(error.description,
                "Number does not belong to this account")

            grp = lidb.lidb_tn_groups.lidb_tn_group.items[0]

            self.assertEqual(grp.telephone_numbers.telephone_number.items[0],
                "4352154856")

            self.assertEqual(grp.subscriber_information, "Steve")
            self.assertEqual(grp.use_type, "RESIDENTIAL")
            self.assertEqual(grp.visibility, "PUBLIC")

            grp = lidb.lidb_tn_groups.lidb_tn_group.items[1]

            self.assertEqual(grp.telephone_numbers.telephone_number.items[0],
                "4352154855")

            self.assertEqual(grp.subscriber_information, "Steve")
            self.assertEqual(grp.use_type, "RESIDENTIAL")
            self.assertEqual(grp.visibility, "PUBLIC")

    def test_lidb_list(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._account.lidbs.get_xpath()
            m.get(url, content=XML_RESPONSE_LIDB_LIST)

            lidbs = self._account.lidbs.list({"telephone_number": "888"})

            lidb = lidbs.items[0]

            self.assertEqual(len(lidbs.items), 2)
            self.assertEqual(lidb.order_id,
                "abe36738-6929-4c6f-926c-88e534e2d46f")
            self.assertEqual(lidb.account_id, "9999999")
            self.assertEqual(lidb.count_of_tns, "0")
            self.assertEqual(lidb.user_id, "team_ua")
            self.assertEqual(lidb.last_modified_date,
                "2014-02-25T16:02:43.195Z")
            self.assertEqual(lidb.order_type, "lidb")
            self.assertEqual(lidb.order_date, "2014-02-25T16:02:43.195Z")
            self.assertEqual(lidb.order_status, "FAILED")
            self.assertEqual(lidb.id, "abe36738-6929-4c6f-926c-88e534e2d46f")

    def test_lidb_post(self):

        order_data = {
            "lidb_tn_groups": {
                "lidb_tn_group": [
                    {
                        "telephone_numbers": {
                            "telephone_number": ["4352154856"]
                        },
                        "subscriber_information": "Steve",
                        "use_type": "RESIDENTIAL",
                        "visibility": "PUBLIC"
                    },
                    {
                        "telephone_numbers": {
                            "telephone_number": ["4352154855"]
                        },
                        "subscriber_information": "Steve",
                        "use_type": "RESIDENTIAL",
                        "visibility": "PUBLIC"
                    }
                ]
            }
        }

        lidb = self._account.lidbs.create(order_data, False)

        grp = lidb.lidb_tn_groups.lidb_tn_group.items[0]
        tns = grp.telephone_numbers.telephone_number.items

        self.assertEqual(tns, ["4352154856"])
        self.assertEqual(grp.subscriber_information, "Steve")
        self.assertEqual(grp.use_type, "RESIDENTIAL")
        self.assertEqual(grp.visibility, "PUBLIC")

        grp = lidb.lidb_tn_groups.lidb_tn_group.items[1]
        tns = grp.telephone_numbers.telephone_number.items

        self.assertEqual(tns, ["4352154855"])
        self.assertEqual(grp.subscriber_information, "Steve")
        self.assertEqual(grp.use_type, "RESIDENTIAL")
        self.assertEqual(grp.visibility, "PUBLIC")

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._account.lidbs.get_xpath()
            m.post(url, content=XML_RESPONSE_LIDB_POST)

            lidb = self._account.lidbs.create(order_data)

            self.assertEqual(lidb.customer_order_id, "testCustomerOrderId")
            self.assertEqual(lidb.order_id,
                "255bda29-fc57-44e8-a6c2-59b45388c6d0")
            self.assertEqual(lidb.last_modified_date,
                "2014-02-20T19:33:17.600Z")
            self.assertEqual(lidb.order_create_date,
                "2014-05-28T14:46:21.724Z")
            self.assertEqual(lidb.processing_status, "RECEIVED")
            self.assertEqual(lidb.created_by_user, "jbm")
            self.assertEqual(lidb.order_complete_date,
                "2014-02-20T19:33:17.600Z")

            grp = lidb.lidb_tn_groups.lidb_tn_group.items[0]
            tns = grp.telephone_numbers.telephone_number.items

            self.assertEqual(tns, ["4082213311"])
            self.assertEqual(grp.subscriber_information, "Fred")
            self.assertEqual(grp.use_type, "BUSINESS")
            self.assertEqual(grp.visibility, "PRIVATE")
            self.assertEqual(grp.full_number, "8042105618")

            grp = lidb.lidb_tn_groups.lidb_tn_group.items[1]
            tns = grp.telephone_numbers.telephone_number.items

            self.assertEqual(tns, ["4082212850", "4082213310"])
            self.assertEqual(grp.subscriber_information, "Fred")
            self.assertEqual(grp.use_type, "RESIDENTIAL")
            self.assertEqual(grp.visibility, "PUBLIC")
            self.assertEqual(grp.full_number, "8042105760")

if __name__ == "__main__":
    main()