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

XML_RESPONSE_CREATE_TN_OPTION_ORDER = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<TnOptionOrderResponse>"
    b"    <TnOptionOrder>"
    b"        <OrderCreateDate>2016-01-15T12:01:14.324Z</OrderCreateDate>"
    b"        <AccountId>14</AccountId>"
    b"        <CreatedByUser>jbm</CreatedByUser>"
    b"        <OrderId>ddbdc72e-dc27-490c-904e-d0c11291b095</OrderId>"
    b"        <LastModifiedDate>2016-01-15T12:01:14.324Z</LastModifiedDate>"
    b"        <ProcessingStatus>RECEIVED</ProcessingStatus>"
    b"        <TnOptionGroups>"
    b"            <TnOptionGroup>"
    b"                <NumberFormat>10digit</NumberFormat>"
    b"                <RPIDFormat>10digit</RPIDFormat>"
    b"                <RewriteUser>testUser1</RewriteUser>"
    b"                <CallForward>6042661720</CallForward>"
    b"                <CallingNameDisplay>on</CallingNameDisplay>"
    b"                <Protected>true</Protected>"
    b"                <Sms>on</Sms>"
    b"                <TelephoneNumbers>"
    b"                    <TelephoneNumber>2018551020</TelephoneNumber>"
    b"                </TelephoneNumbers>"
    b"            </TnOptionGroup>"
    b"            <TnOptionGroup>"
    b"                <CallingNameDisplay>off</CallingNameDisplay>"
    b"                <Protected>false</Protected>"
    b"                <Sms>off</Sms>"
    b"                <TelephoneNumbers>"
    b"                    <TelephoneNumber>2018551025</TelephoneNumber>"
    b"                </TelephoneNumbers>"
    b"            </TnOptionGroup>"
    b"        </TnOptionGroups>"
    b"        <ErrorList/>"
    b"    </TnOptionOrder>"
    b"</TnOptionOrderResponse>"
)

XML_RESPONSE_LIST_TN_OPTION_ORDER_SUMMARY = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<TnOptionOrders>"
    b"    <TotalCount>2</TotalCount>"
    b"    <TnOptionOrderSummary>"
    b"        <accountId>14</accountId>"
    b"        <CountOfTNs>2</CountOfTNs>"
    b"        <userId>jbm</userId>"
    b"        <lastModifiedDate>2016-01-15T12:01:14.363Z</lastModifiedDate>"
    b"        <OrderDate>2016-01-15T12:01:14.324Z</OrderDate>"
    b"        <OrderType>tn_option</OrderType>"
    b"        <OrderStatus>FAILED</OrderStatus>"
    b"        <OrderId>ddbdc72e-dc27-490c-904e-d0c11291b095</OrderId>"
    b"    </TnOptionOrderSummary>"
    b"    <TnOptionOrderSummary>"
    b"        <accountId>14</accountId>"
    b"        <CountOfTNs>3</CountOfTNs>"
    b"        <userId>jbm</userId>"
    b"        <lastModifiedDate>2016-01-15T11:22:58.969Z</lastModifiedDate>"
    b"        <OrderDate>2016-01-15T11:22:58.789Z</OrderDate>"
    b"        <OrderType>tn_option</OrderType>"
    b"        <OrderStatus>COMPLETE</OrderStatus>"
    b"        <OrderId>409033ee-88ec-43e3-85f3-538f30733963</OrderId>"
    b"    </TnOptionOrderSummary>"
    b"</TnOptionOrders>"
)

XML_RESPONSE_LIST_TN_OPTION_ORDER = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<TnOptionOrders>"
    b"    <TotalCount>2</TotalCount>"
    b"    <TnOptionOrder>"
    b"        <OrderCreateDate>2016-01-15T12:01:14.324Z</OrderCreateDate>"
    b"        <AccountId>14</AccountId>"
    b"        <CreatedByUser>jbm</CreatedByUser>"
    b"        <OrderId>ddbdc72e-dc27-490c-904e-d0c11291b095</OrderId>"
    b"        <LastModifiedDate>2016-01-15T12:01:14.363Z</LastModifiedDate>"
    b"        <ProcessingStatus>FAILED</ProcessingStatus>"
    b"        <TnOptionGroups>"
    b"            <TnOptionGroup>"
    b"                <NumberFormat>10digit</NumberFormat>"
    b"                <RPIDFormat>10digit</RPIDFormat>"
    b"                <RewriteUser>testUser1</RewriteUser>"
    b"                <CallForward>6042661720</CallForward>"
    b"                <CallingNameDisplay>on</CallingNameDisplay>"
    b"                <Protected>true</Protected>"
    b"                <Sms>on</Sms>"
    b"                <FinalDestinationURI>sip:+12345678901@1.2.3.4:5060</FinalDestinationURI>"
    b"                <TelephoneNumbers>"
    b"                    <TelephoneNumber>2018551020</TelephoneNumber>"
    b"                </TelephoneNumbers>"
    b"            </TnOptionGroup>"
    b"            <TnOptionGroup>"
    b"                <CallingNameDisplay>off</CallingNameDisplay>"
    b"                <Protected>false</Protected>"
    b"                <Sms>off</Sms>"
    b"                <TelephoneNumbers>"
    b"                    <TelephoneNumber>2018551025</TelephoneNumber>"
    b"                </TelephoneNumbers>"
    b"            </TnOptionGroup>"
    b"        </TnOptionGroups>"
    b"        <ErrorList>"
    b"            <Error>"
    b"                <Code>5076</Code>"
    b"                <Description>Telephone number is not available.</Description>"
    b"                <TelephoneNumber>2018551025</TelephoneNumber>"
    b"            </Error>"
    b"            <Error>"
    b"                <Code>5076</Code>"
    b"                <Description>Telephone number is not available.</Description>"
    b"                <TelephoneNumber>2018551020</TelephoneNumber>"
    b"            </Error>"
    b"        </ErrorList>"
    b"    </TnOptionOrder>"
    b"    <TnOptionOrder>"
    b"        <OrderCreateDate>2016-01-15T11:22:58.789Z</OrderCreateDate>"
    b"        <AccountId>14</AccountId>"
    b"        <CreatedByUser>jbm</CreatedByUser>"
    b"        <OrderId>409033ee-88ec-43e3-85f3-538f30733963</OrderId>"
    b"        <LastModifiedDate>2016-01-15T11:22:58.969Z</LastModifiedDate>"
    b"        <ProcessingStatus>COMPLETE</ProcessingStatus>"
    b"        <TnOptionGroups>"
    b"            <TnOptionGroup>"
    b"                <CallingNameDisplay>on</CallingNameDisplay>"
    b"                <TelephoneNumbers>"
    b"                    <TelephoneNumber>2174101601</TelephoneNumber>"
    b"                </TelephoneNumbers>"
    b"            </TnOptionGroup>"
    b"            <TnOptionGroup>"
    b"                <CallingNameDisplay>off</CallingNameDisplay>"
    b"                <TelephoneNumbers>"
    b"                    <TelephoneNumber>2174101602</TelephoneNumber>"
    b"                </TelephoneNumbers>"
    b"            </TnOptionGroup>"
    b"            <TnOptionGroup>"
    b"                <CallingNameDisplay>systemdefault</CallingNameDisplay>"
    b"                <TelephoneNumbers>"
    b"                    <TelephoneNumber>2174101603</TelephoneNumber>"
    b"                </TelephoneNumbers>"
    b"            </TnOptionGroup>"
    b"        </TnOptionGroups>"
    b"        <ErrorList/>"
    b"    </TnOptionOrder>"
    b"</TnOptionOrders>"
)

XML_RESPONSE_GET_TN_OPTION_ORDER = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<TnOptionOrder>"
    b"    <OrderCreateDate>2016-01-15T11:22:58.789Z</OrderCreateDate>"
    b"    <AccountId>14</AccountId>"
    b"    <CreatedByUser>jbm</CreatedByUser>"
    b"    <OrderId>409033ee-88ec-43e3-85f3-538f30733963</OrderId>"
    b"    <LastModifiedDate>2016-01-15T11:22:58.969Z</LastModifiedDate>"
    b"    <ProcessingStatus>COMPLETE</ProcessingStatus>"
    b"    <TnOptionGroups>"
    b"        <TnOptionGroup>"
    b"            <CallingNameDisplay>on</CallingNameDisplay>"
    b"            <Sms>on</Sms>"
    b"            <TelephoneNumbers>"
    b"                <TelephoneNumber>2174101601</TelephoneNumber>"
    b"            </TelephoneNumbers>"
    b"        </TnOptionGroup>"
    b"        <TnOptionGroup>"
    b"            <CallingNameDisplay>off</CallingNameDisplay>"
    b"            <TelephoneNumbers>"
    b"                <TelephoneNumber>2174101602</TelephoneNumber>"
    b"            </TelephoneNumbers>"
    b"        </TnOptionGroup>"
    b"        <TnOptionGroup>"
    b"            <CallingNameDisplay>systemdefault</CallingNameDisplay>"
    b"            <FinalDestinationURI>sip:+12345678901@1.2.3.4:5060</FinalDestinationURI>"
    b"            <TelephoneNumbers>"
    b"                <TelephoneNumber>2174101603</TelephoneNumber>"
    b"            </TelephoneNumbers>"
    b"        </TnOptionGroup>"
    b"    </TnOptionGroups>"
    b"    <ErrorList/>"
    b"    <Warnings>"
    b"        <Warning>"
    b"            <TelephoneNumber>2174101601</TelephoneNumber>"
    b"            <Description>SMS is already Enabled or number is in processing.</Description>"
    b"        </Warning>"
    b"    </Warnings>"
    b"</TnOptionOrder>"
)

class TnOptionOrdersTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._account

    def test_create_tn_option_order(self):
        with requests_mock.Mocker() as m:
            url = self._client.config.url + self._account._tn_option_orders.get_xpath()
            m.post(url, content=XML_RESPONSE_CREATE_TN_OPTION_ORDER)
            order = self._account.tn_option_orders.create({
                "customer_order_id": "12345",
                "tn_option_groups": {
                    "tn_option_group": [
                        {
                            "number_format": "10digit"
                        }
                    ]
                }
            })

            self.assertEqual(order.account_id, '14')
            self.assertEqual(order.order_create_date, "2016-01-15T12:01:14.324Z")

    def test_get_tn_option_orders_summary(self):
        with requests_mock.Mocker() as m:
            url = self._client.config.url + self._account._tn_option_orders.get_xpath()
            m.get(url, content=XML_RESPONSE_LIST_TN_OPTION_ORDER_SUMMARY)
            order = self._account.tn_option_orders.list()

            self.assertEqual(order.total_count, '2')
            self.assertEqual(order.tn_option_order_summary.items[0].account_id, '14')

    def test_get_tn_option_orders(self):
        with requests_mock.Mocker() as m:
            url = self._client.config.url + self._account._tn_option_orders.get_xpath()
            m.get(url, content=XML_RESPONSE_LIST_TN_OPTION_ORDER)
            order = self._account.tn_option_orders.list()

            self.assertEqual(order.total_count, '2')
            self.assertEqual(order.tn_option_order.items[0].account_id, '14')
            self.assertEqual(order.tn_option_order.items[0].tn_option_groups.tn_option_group.items[0].number_format, '10digit')

    def test_get_tn_option_order(self):
        with requests_mock.Mocker() as m:
            url = self._client.config.url + self._account._tn_option_orders.get_xpath() + "/id"
            m.get(url, content=XML_RESPONSE_GET_TN_OPTION_ORDER)
            order = self._account.tn_option_orders.get("id")

            self.assertEqual(order.order_create_date, "2016-01-15T11:22:58.789Z")
            self.assertEqual(order.warnings.warning.items[0].telephone_number, "2174101601")
