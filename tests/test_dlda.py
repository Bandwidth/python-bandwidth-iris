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

XML_RESPONSE_DLDA_GET = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\" ?>"
    b"<DldaOrderResponse><DldaOrder>"
    b"<CustomerOrderId>5a88d16d-f8a9-45c5-a5db-137d700c6a22</CustomerOrderId>"
    b"<OrderCreateDate>2014-07-10T12:38:11.833Z</OrderCreateDate>"
    b"<AccountId>14</AccountId><CreatedByUser>jbm</CreatedByUser>"
    b"<OrderId>ea9e90c2-77a4-4f82-ac47-e1c5bb1311f4</OrderId>"
    b"<LastModifiedDate>2014-07-10T12:38:11.833Z</LastModifiedDate>"
    b"<ProcessingStatus>RECEIVED</ProcessingStatus><DldaTnGroups>"
    b"<DldaTnGroup><TelephoneNumbers>"
    b"<TelephoneNumber>2053778335</TelephoneNumber>"
    b"<TelephoneNumber>2053865784</TelephoneNumber></TelephoneNumbers>"
    b"<AccountType>BUSINESS</AccountType><ListingType>LISTED</ListingType>"
    b"<ListingName><FirstName>Joe</FirstName><LastName>Smith</LastName>"
    b"</ListingName><ListAddress>true</ListAddress><Address>"
    b"<HouseNumber>12</HouseNumber><StreetName>ELM</StreetName>"
    b"<City>New York</City><StateCode>NY</StateCode><Zip>10007</Zip>"
    b"<Country>United States</Country><AddressType>Dlda</AddressType>"
    b"</Address></DldaTnGroup></DldaTnGroups></DldaOrder>"
    b"</DldaOrderResponse>"
)

XML_RESPONSE_DLDA_HISTORY = (
    b"<?xml version=\"1.0\"?> <OrderHistoryWrapper><OrderHistory>"
    b"<OrderDate>2014-09-04T16:28:11.320Z</OrderDate>"
    b"<Note>The DL/DA request has been received</Note>"
    b"<Author>jbm</Author><Status>RECEIVED</Status></OrderHistory>"
    b"<OrderHistory><OrderDate>2014-09-04T16:28:18.742Z</OrderDate>"
    b"<Note>The DL/DA request is being processed by our 3rd party supplier"
    b"</Note><Author>jbm</Author><Status>PROCESSING</Status> </OrderHistory>"
    b"<OrderHistory><OrderDate>2014-09-05T19:00:17.968Z</OrderDate>"
    b"<Note>The DL/DA request is complete for all TNs</Note>"
    b"<Author>jbm</Author><Status>COMPLETE</Status></OrderHistory>"
    b"</OrderHistoryWrapper>"
)

XML_RESPONSE_DLDA_LIST = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\" ?>"
    b"<ResponseSelectWrapper><ListOrderIdUserIdDate>"
    b"<TotalCount>3</TotalCount><OrderIdUserIdDate>"
    b"<accountId>14</accountId><CountOfTNs>2</CountOfTNs>"
    b"<userId>team_ua</userId>"
    b"<lastModifiedDate>2014-07-07T10:06:43.427Z</lastModifiedDate>"
    b"<OrderType>dlda</OrderType>"
    b"<OrderDate>2014-07-07T10:06:43.427Z</OrderDate>"
    b"<orderId>37a6447c-1a0b-4be9-ba89-3f5cb0aea142</orderId>"
    b"<OrderStatus>FAILED</OrderStatus></OrderIdUserIdDate>"
    b"<OrderIdUserIdDate><accountId>14</accountId>"
    b"<CountOfTNs>2</CountOfTNs><userId>team_ua</userId>"
    b"<lastModifiedDate>2014-07-07T10:05:56.595Z</lastModifiedDate>"
    b"<OrderType>dlda</OrderType>"
    b"<OrderDate>2014-07-07T10:05:56.595Z</OrderDate>"
    b"<orderId>743b0e64-3350-42e4-baa6-406dac7f4a85</orderId>"
    b"<OrderStatus>RECEIVED</OrderStatus></OrderIdUserIdDate>"
    b"<OrderIdUserIdDate><accountId>14</accountId>"
    b"<CountOfTNs>2</CountOfTNs><userId>team_ua</userId>"
    b"<lastModifiedDate>2014-07-07T09:32:17.234Z</lastModifiedDate>"
    b"<OrderType>dlda</OrderType>"
    b"<OrderDate>2014-07-07T09:32:17.234Z</OrderDate>"
    b"<orderId>f71eb4d2-bfef-4384-957f-45cd6321185e</orderId>"
    b"<OrderStatus>RECEIVED</OrderStatus></OrderIdUserIdDate>"
    b"</ListOrderIdUserIdDate></ResponseSelectWrapper>"
)

XML_RESPONSE_DLDA_POST = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\" ?>"
    b"<DldaOrderResponse><DldaOrder>"
    b"<CustomerOrderId>5a88d16d-f8a9-45c5-a5db-137d700c6a22</CustomerOrderId>"
    b"<OrderCreateDate>2014-07-10T12:38:11.833Z</OrderCreateDate>"
    b"<AccountId>14</AccountId><CreatedByUser>jbm</CreatedByUser>"
    b"<OrderId>ea9e90c2-77a4-4f82-ac47-e1c5bb1311f4</OrderId>"
    b"<LastModifiedDate>2014-07-10T12:38:11.833Z</LastModifiedDate>"
    b"<ProcessingStatus>RECEIVED</ProcessingStatus><DldaTnGroups>"
    b"<DldaTnGroup><TelephoneNumbers>"
    b"<TelephoneNumber>2053778335</TelephoneNumber>"
    b"<TelephoneNumber>2053865784</TelephoneNumber></TelephoneNumbers>"
    b"<AccountType>BUSINESS</AccountType><ListingType>LISTED</ListingType>"
    b"<ListingName><FirstName>Joe</FirstName><LastName>Smith</LastName>"
    b"</ListingName><ListAddress>true</ListAddress><Address>"
    b"<HouseNumber>12</HouseNumber><StreetName>ELM</StreetName>"
    b"<City>New York</City><StateCode>NY</StateCode><Zip>10007</Zip>"
    b"<Country>United States</Country><AddressType>Dlda</AddressType>"
    b"</Address></DldaTnGroup></DldaTnGroups></DldaOrder>"
    b"</DldaOrderResponse>"
)

class ClassDldaTest(TestCase):

    """Test DLDA orders"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._client
        del cls._account

    def test_dlda_get(self):

        with requests_mock.Mocker() as m:

            dlda = self._account.dldas.create()
            dlda.id = "ea9e90c2-77a4-4f82-ac47-e1c5bb1311f4"

            url = self._client.config.url + dlda.get_xpath()
            m.get(url, content=XML_RESPONSE_DLDA_GET)

            dlda = self._account.dldas.get(dlda.id)

            self.assertEqual(dlda.id, "ea9e90c2-77a4-4f82-ac47-e1c5bb1311f4")
            self.assertEqual(dlda.customer_order_id,
                "5a88d16d-f8a9-45c5-a5db-137d700c6a22")
            self.assertEqual(dlda.order_create_date,
                "2014-07-10T12:38:11.833Z")
            self.assertEqual(dlda.account_id, "14")
            self.assertEqual(dlda.created_by_user, "jbm")
            self.assertEqual(dlda.order_id,
                "ea9e90c2-77a4-4f82-ac47-e1c5bb1311f4")
            self.assertEqual(dlda.last_modified_date,
                "2014-07-10T12:38:11.833Z")
            self.assertEqual(dlda.processing_status, "RECEIVED")

            grp = dlda.dlda_tn_groups.dlda_tn_group.items[0]

            self.assertEqual(
                grp.telephone_numbers.telephone_number.items,
                ["2053778335","2053865784"]
            )

            self.assertEqual(grp.account_type, "BUSINESS")
            self.assertEqual(grp.listing_type, "LISTED")
            self.assertEqual(grp.list_address, "true")

            lname = grp.listing_name

            self.assertEqual(lname.first_name, "Joe")
            self.assertEqual(lname.last_name, "Smith")

            addr = grp.address

            self.assertEqual(addr.city, "New York")
            self.assertEqual(addr.house_number, "12")
            self.assertEqual(addr.street_name, "ELM")
            self.assertEqual(addr.state_code, "NY")
            self.assertEqual(addr.zip, "10007")
            self.assertEqual(addr.country, "United States")
            self.assertEqual(addr.address_type, "Dlda")

    def test_dlda_list(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._account.dldas.get_xpath()
            m.get(url, content=XML_RESPONSE_DLDA_LIST)

            dldas = self._account.dldas.list()

            dlda = dldas.items[0]

            self.assertEqual(len(dldas.items), 3)
            self.assertEqual(dlda.id, "37a6447c-1a0b-4be9-ba89-3f5cb0aea142")
            self.assertEqual(dlda.account_id, "14")
            self.assertEqual(dlda.count_of_tns, "2")
            self.assertEqual(dlda.user_id, "team_ua")
            self.assertEqual(dlda.last_modified_date,
                "2014-07-07T10:06:43.427Z")
            self.assertEqual(dlda.order_type, "dlda")
            self.assertEqual(dlda.order_date, "2014-07-07T10:06:43.427Z")
            self.assertEqual(dlda.order_id, "37a6447c-1a0b-4be9-ba89-3f5cb0aea142")
            self.assertEqual(dlda.order_status, "FAILED")

    def test_dlda_post(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._account.dldas.get_xpath()
            m.post(url, content=XML_RESPONSE_DLDA_POST)

            order_data = {
                "customer_order_id": "123",
                "dlda_tn_groups": {
                    "dlda_tn_group": [{
                        "telephone_numbers": {
                            "telephone_number": ["4352154856"]
                        },
                        "account_type": "RESIDENTIAL",
                        "listing_type": "LISTED",
                        "list_address": "true",
                        "listing_name": {
                            "first_name": "first name",
                            "first_name2": "first name2",
                            "last_name": "last name",
                            "designation": "designation",
                            "title_of_lineage": "title of lineage",
                            "title_of_address": "title of address",
                            "title_of_address2": "title of address2",
                            "title_of_lineage_name2":"title of lineage name2",
                            "title_of_address_name2":"title of address name2",
                            "title_of_address2_name2":
                                "title of address2 name2",
                            "place_listing_as": "place listing as"
                        },
                        "address": {
                            "house_prefix": "house prefix",
                            "house_number": "915",
                            "house_suffix": "house suffix",
                            "pre_directional": "pre directional",
                            "street_name": "street name",
                            "street_suffix": "street suffix",
                            "post_directional": "post directional",
                            "address_line2": "address line2",
                            "city": "city",
                            "state_code": "state code",
                            "zip": "zip",
                            "plus_four": "plus four",
                            "country": "country",
                            "address_type": "address type"
                        }
                    }]
                }
            }

            dlda = self._account.dldas.create(order_data, False)

            self.assertEqual(dlda.customer_order_id, "123")
            grp = dlda.dlda_tn_groups.dlda_tn_group.items[0]
            self.assertEqual(grp.telephone_numbers.telephone_number.items,
                ["4352154856"])
            self.assertEqual(grp.account_type, "RESIDENTIAL")
            self.assertEqual(grp.listing_type, "LISTED")
            self.assertEqual(grp.list_address, "true")

            name = grp.listing_name

            self.assertEqual(name.first_name, "first name")
            self.assertEqual(name.first_name2, "first name2")
            self.assertEqual(name.last_name, "last name")
            self.assertEqual(name.designation, "designation")
            self.assertEqual(name.title_of_lineage, "title of lineage")
            self.assertEqual(name.title_of_address, "title of address")
            self.assertEqual(name.title_of_address2, "title of address2")
            self.assertEqual(name.title_of_lineage_name2,
                "title of lineage name2")
            self.assertEqual(name.title_of_address_name2,
                "title of address name2")
            self.assertEqual(name.title_of_address2_name2,
                "title of address2 name2")
            self.assertEqual(name.place_listing_as, "place listing as")

            addr = grp.address

            self.assertEqual(addr.house_prefix, "house prefix")
            self.assertEqual(addr.house_number, "915")
            self.assertEqual(addr.house_suffix, "house suffix")
            self.assertEqual(addr.pre_directional, "pre directional")
            self.assertEqual(addr.street_name, "street name")
            self.assertEqual(addr.street_suffix, "street suffix")
            self.assertEqual(addr.post_directional, "post directional")
            self.assertEqual(addr.address_line2, "address line2")
            self.assertEqual(addr.city, "city")
            self.assertEqual(addr.state_code, "state code")
            self.assertEqual(addr.zip, "zip")
            self.assertEqual(addr.plus_four, "plus four")
            self.assertEqual(addr.country, "country")
            self.assertEqual(addr.address_type, "address type")

            dlda = self._account.dldas.create(order_data)

            self.assertEqual(dlda.customer_order_id,
                "5a88d16d-f8a9-45c5-a5db-137d700c6a22")
            self.assertEqual(dlda.order_create_date,
                "2014-07-10T12:38:11.833Z")
            self.assertEqual(dlda.account_id, "14")
            self.assertEqual(dlda.created_by_user, "jbm")
            self.assertEqual(dlda.order_id,
                "ea9e90c2-77a4-4f82-ac47-e1c5bb1311f4")
            self.assertEqual(dlda.last_modified_date,
                "2014-07-10T12:38:11.833Z")
            self.assertEqual(dlda.processing_status, "RECEIVED")

            grp = dlda.dlda_tn_groups.dlda_tn_group.items[0]

            self.assertEqual(grp.telephone_numbers.telephone_number.items,
                ["2053778335","2053865784"])
            self.assertEqual(grp.account_type, "BUSINESS")
            self.assertEqual(grp.listing_type, "LISTED")
            self.assertEqual(grp.list_address, "true")

            name = grp.listing_name

            self.assertEqual(name.first_name, "Joe")
            self.assertEqual(name.last_name, "Smith")

            addr = grp.address

            self.assertEqual(addr.city, "New York")
            self.assertEqual(addr.house_number, "12")
            self.assertEqual(addr.street_name, "ELM")
            self.assertEqual(addr.state_code, "NY")
            self.assertEqual(addr.zip, "10007")
            self.assertEqual(addr.country, "United States")
            self.assertEqual(addr.address_type, "Dlda")

    def test_dlda_put(self):

        order_data = {
            "order_id": "7802373f-4f52-4387-bdd1-c5b74833d6e2",
            "customer_order_id": "123",
            "dlda_tn_groups": {
                "dlda_tn_group": [{
                    "telephone_numbers": {
                        "telephone_number": ["4352154856"]
                    },
                    "account_type": "RESIDENTIAL",
                    "listing_type": "LISTED",
                    "list_address": "true",
                    "listing_name": {
                        "first_name": "first name",
                        "first_name2": "first name2",
                        "last_name": "last name",
                        "designation": "designation",
                        "title_of_lineage": "title of lineage",
                        "title_of_address": "title of address",
                        "title_of_address2": "title of address2",
                        "title_of_lineage_name2":"title of lineage name2",
                        "title_of_address_name2":"title of address name2",
                        "title_of_address2_name2": "title of address2 name2",
                        "place_listing_as": "place listing as"
                    },
                    "address": {
                        "house_prefix": "house prefix",
                        "house_number": "915",
                        "house_suffix": "house suffix",
                        "pre_directional": "pre directional",
                        "street_name": "street name",
                        "street_suffix": "street suffix",
                        "post_directional": "post directional",
                        "address_line2": "address line2",
                        "city": "city",
                        "state_code": "state code",
                        "zip": "zip",
                        "plus_four": "plus four",
                        "country": "country",
                        "address_type": "address type"
                    }
                }]
            }
        }

        dlda = self._account.dldas.create(order_data, False)

        self.assertEqual(dlda.customer_order_id, "123")
        self.assertEqual(dlda.order_id,
            "7802373f-4f52-4387-bdd1-c5b74833d6e2")

        grp = dlda.dlda_tn_groups.dlda_tn_group.items[0]
        self.assertEqual(grp.telephone_numbers.telephone_number.items,
            ["4352154856"])
        self.assertEqual(grp.account_type, "RESIDENTIAL")
        self.assertEqual(grp.listing_type, "LISTED")
        self.assertEqual(grp.list_address, "true")

        name = grp.listing_name

        self.assertEqual(name.first_name, "first name")
        self.assertEqual(name.first_name2, "first name2")
        self.assertEqual(name.last_name, "last name")
        self.assertEqual(name.designation, "designation")
        self.assertEqual(name.title_of_lineage, "title of lineage")
        self.assertEqual(name.title_of_address, "title of address")
        self.assertEqual(name.title_of_address2, "title of address2")
        self.assertEqual(name.title_of_lineage_name2,
            "title of lineage name2")
        self.assertEqual(name.title_of_address_name2,
            "title of address name2")
        self.assertEqual(name.title_of_address2_name2,
            "title of address2 name2")
        self.assertEqual(name.place_listing_as, "place listing as")

        addr = grp.address

        self.assertEqual(addr.house_prefix, "house prefix")
        self.assertEqual(addr.house_number, "915")
        self.assertEqual(addr.house_suffix, "house suffix")
        self.assertEqual(addr.pre_directional, "pre directional")
        self.assertEqual(addr.street_name, "street name")
        self.assertEqual(addr.street_suffix, "street suffix")
        self.assertEqual(addr.post_directional, "post directional")
        self.assertEqual(addr.address_line2, "address line2")
        self.assertEqual(addr.city, "city")
        self.assertEqual(addr.state_code, "state code")
        self.assertEqual(addr.zip, "zip")
        self.assertEqual(addr.plus_four, "plus four")
        self.assertEqual(addr.country, "country")
        self.assertEqual(addr.address_type, "address type")

        self.assertEqual(dlda.get_xpath(),
            self._account.get_xpath() + self._account.dldas._xpath +
            dlda._xpath.format(dlda.id))

        with requests_mock.Mocker() as m:

            url = self._client.config.url + dlda.get_xpath()
            m.put(url, content = XML_RESPONSE_DLDA_GET)

            dlda.save()

if __name__ == "__main__":
    main()