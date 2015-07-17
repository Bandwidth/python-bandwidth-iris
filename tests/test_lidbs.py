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
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<LidbOrder><OrderCreateDate>2015-06-21T04:52:33.191Z</OrderCreateDate>"
    "<AccountId>9500249</AccountId><CreatedByUser>byo_dev</CreatedByUser>"
    "<OrderId>7802373f-4f52-4387-bdd1-c5b74833d6e2</OrderId>"
    "<LastModifiedDate>2015-06-21T04:52:33.191Z</LastModifiedDate>"
    "<ErrorList><Error><Code>11014</Code>"
    "<Description>Number does not belong to this account</Description>"
    "<TelephoneNumber>4352154856</TelephoneNumber></Error><Error>"
    "<Code>11014</Code>"
    "<Description>Number does not belong to this account</Description>"
    "<TelephoneNumber>4352154855</TelephoneNumber></Error></ErrorList>"
    "<ProcessingStatus>FAILED</ProcessingStatus><LidbTnGroups><LidbTnGroup>"
    "<TelephoneNumbers><TelephoneNumber>4352154856</TelephoneNumber>"
    "</TelephoneNumbers><SubscriberInformation>Steve</SubscriberInformation>"
    "<UseType>RESIDENTIAL</UseType><Visibility>PUBLIC</Visibility>"
    "</LidbTnGroup><LidbTnGroup><TelephoneNumbers>"
    "<TelephoneNumber>4352154855</TelephoneNumber></TelephoneNumbers>"
    "<SubscriberInformation>Steve</SubscriberInformation>"
    "<UseType>RESIDENTIAL</UseType><Visibility>PUBLIC</Visibility>"
    "</LidbTnGroup></LidbTnGroups></LidbOrder>"
)

XML_RESPONSE_LIDB_LIST = (
    "<?xml version=\"1.0\"?><ResponseSelectWrapper><ListOrderIdUserIdDate>"
    "<TotalCount>2122</TotalCount><OrderIdUserIdDate>"
    "<accountId>9999999</accountId><CountOfTNs>0</CountOfTNs>"
    "<lastModifiedDate>2014-02-25T16:02:43.195Z</lastModifiedDate>"
    "<OrderType>lidb</OrderType>"
    "<OrderDate>2014-02-25T16:02:43.195Z</OrderDate>"
    "<orderId>abe36738-6929-4c6f-926c-88e534e2d46f</orderId>"
    "<OrderStatus>FAILED</OrderStatus><TelephoneNumberDetails/>"
    "<userId>team_ua</userId></OrderIdUserIdDate><OrderIdUserIdDate>"
    "<accountId>9999999</accountId><CountOfTNs>0</CountOfTNs>"
    "<lastModifiedDate>2014-02-25T16:02:39.021Z</lastModifiedDate>"
    "<OrderType>lidb</OrderType>"
    "<OrderDate>2014-02-25T16:02:39.021Z</OrderDate>"
    "<orderId>ba5b6297-139b-4430-aab0-9ff02c4362f4</orderId>"
    "<OrderStatus>FAILED</OrderStatus><userId>team_ua</userId>"
    "</OrderIdUserIdDate></ListOrderIdUserIdDate></ResponseSelectWrapper>"
)

XML_RESPONSE_LIDB_POST = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<LidbOrder><CustomerOrderId>testCustomerOrderId</CustomerOrderId>"
    "<orderId>255bda29-fc57-44e8-a6c2-59b45388c6d0</orderId>"
    "<OrderCreateDate>2014-05-28T14:46:21.724Z</OrderCreateDate>"
    "<ProcessingStatus>RECEIVED</ProcessingStatus>"
    "<CreatedByUser>jbm</CreatedByUser>"
    "<LastModifiedDate>2014-02-20T19:33:17.600Z</LastModifiedDate>"
    "<OrderCompleteDate>2014-02-20T19:33:17.600Z</OrderCompleteDate>"
    "<ErrorList/><LidbTnGroups><LidbTnGroup><TelephoneNumbers>"
    "<TelephoneNumber>4082213311</TelephoneNumber></TelephoneNumbers>"
    "<FullNumber>8042105618</FullNumber>"
    "<SubscriberInformation>Fred</SubscriberInformation>"
    "<UseType>BUSINESS</UseType><Visibility>PRIVATE</Visibility>"
    "</LidbTnGroup><LidbTnGroup><TelephoneNumbers>"
    "<TelephoneNumber>4082212850</TelephoneNumber>"
    "<TelephoneNumber>4082213310</TelephoneNumber></TelephoneNumbers>"
    "<FullNumber>8042105760</FullNumber>"
    "<SubscriberInformation>Fred</SubscriberInformation>"
    "<UseType>RESIDENTIAL</UseType><Visibility>PUBLIC</Visibility>"
    "</LidbTnGroup></LidbTnGroups></LidbOrder>"
)

class ClassLidbsTest(TestCase):

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

        lidb = self._account.lidbs.create()
        lidb.id = "7802373f-4f52-4387-bdd1-c5b74833d6e2"

        self.assertEquals(lidb.get_xpath(),
            self._account.get_xpath() + self._account.lidbs._xpath +
            lidb._xpath.format(lidb.id))

        url = self._client.config.url + lidb.get_xpath()

        with requests_mock.Mocker() as m:

            m.get(url, content=XML_RESPONSE_LIDB_GET)

            lidb = self._account.lidbs.get(
                "7802373f-4f52-4387-bdd1-c5b74833d6e2")

            self.assertEquals(m.request_history[0].method, "GET")

            self.assertEquals(lidb.order_id,
                "7802373f-4f52-4387-bdd1-c5b74833d6e2")
            self.assertEquals(lidb.account_id, "9500249")
            self.assertEquals(lidb.last_modified_date,
                "2015-06-21T04:52:33.191Z")
            self.assertEquals(lidb.order_create_date,
                "2015-06-21T04:52:33.191Z")
            self.assertEquals(lidb.processing_status, "FAILED")
            self.assertEquals(lidb.created_by_user, "byo_dev")

            error = lidb.error_list.error.items[0]

            self.assertEquals(error.telephone_number, "4352154856")
            self.assertEquals(error.code, "11014")
            self.assertEquals(error.description,
                "Number does not belong to this account")

            error = lidb.error_list.error.items[1]

            self.assertEquals(error.telephone_number, "4352154855")
            self.assertEquals(error.code, "11014")
            self.assertEquals(error.description,
                "Number does not belong to this account")

            grp = lidb.lidb_tn_groups.lidb_tn_group.items[0]

            self.assertEquals(grp.telephone_numbers.telephone_number.items[0],
                "4352154856")

            self.assertEquals(grp.subscriber_information, "Steve")
            self.assertEquals(grp.use_type, "RESIDENTIAL")
            self.assertEquals(grp.visibility, "PUBLIC")

            grp = lidb.lidb_tn_groups.lidb_tn_group.items[1]

            self.assertEquals(grp.telephone_numbers.telephone_number.items[0],
                "4352154855")

            self.assertEquals(grp.subscriber_information, "Steve")
            self.assertEquals(grp.use_type, "RESIDENTIAL")
            self.assertEquals(grp.visibility, "PUBLIC")

if __name__ == "__main__":
    main()