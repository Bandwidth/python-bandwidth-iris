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

XML_RESPONSE_ACTIVATION_STATUS = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<ActivationStatusResponse><ActivationStatus>"
    b"<AutoActivationDate>2014-08-29T18:30:00+03:00</AutoActivationDate>"
    b"<ActivatedTelephoneNumbersList>"
    b"<TelephoneNumber>6052609021</TelephoneNumber>"
    b"<TelephoneNumber>6052609021</TelephoneNumber>"
    b"</ActivatedTelephoneNumbersList><NotYetActivatedTelephoneNumbersList/>"
    b"</ActivationStatus></ActivationStatusResponse>"
)

XML_RESPONSE_HISTORY = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<OrderHistoryWrapper><OrderHistory>"
    b"<OrderDate>2015-06-03T15:06:35.765Z</OrderDate>"
    b"<Note>LOA required</Note><Author>byo_dev</Author>"
    b"<Status>PENDING_DOCUMENTS</Status></OrderHistory><OrderHistory>"
    b"<OrderDate>2015-06-03T15:06:36.234Z</OrderDate>"
    b"<Note>Order has been created</Note><Author>System</Author>"
    b"<Status>SUBMITTED</Status>"
    b"<Difference>LoaDate: Wed Jun 03 15:06:35 UTC 2015</Difference>"
    b"</OrderHistory></OrderHistoryWrapper>"
)

XML_RESPONSE_LNP_UPDATE = (
    b"<?xml version=\"1.0\"?><LnpOrderResponse>"
    b"<OrderId>0fe651a2-6ffc-4758-b7b7-e3eed66409ec</OrderId><Status>"
    b"<Code>200</Code>"
    b"<Description>Supp request received.</Description></Status>"
    b"<ProcessingStatus>REQUESTED_SUPP</ProcessingStatus>"
    b"<RequestedFocDate>2012-08-30T00:00:00Z</RequestedFocDate>"
    b"</LnpOrderResponse>"
)

XML_RESPONSE_LOAS_GET = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<FileListResponse><FileCount>0</FileCount><ResultCode>0</ResultCode>"
    b"<ResultMessage>No LOA files found for order</ResultMessage>"
    b"</FileListResponse>"
)

XML_RESPONSE_META_GET = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<FileMetaData><DocumentName>test.txt</DocumentName>"
    b"<DocumentType>LOA</DocumentType></FileMetaData>"
)

XML_RESPONSE_PORTIN_POST = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<LnpOrderResponse>"
    b"<OrderId>d28b36f7-fa96-49eb-9556-a40fca49f7c6</OrderId><Status>"
    b"<Code>201</Code>"
    b"<Description></Description></Status>"
    b"<ProcessingStatus>PENDING_DOCUMENTS</ProcessingStatus>"
    b"<LoaAuthorizingPerson>John Doe</LoaAuthorizingPerson><Subscriber>"
    b"<SubscriberType>BUSINESS</SubscriberType>"
    b"<BusinessName>Acme Corporation</BusinessName><ServiceAddress>"
    b"<HouseNumber>1623</HouseNumber><StreetName>Brockton Ave #1</StreetName>"
    b"<City>Los Angeles</City><StateCode>CA</StateCode><Zip>90025</Zip>"
    b"<Country>USA</Country></ServiceAddress></Subscriber>"
    b"<BillingTelephoneNumber>6882015002</BillingTelephoneNumber>"
    b"<ListOfPhoneNumbers><PhoneNumber>6882015025</PhoneNumber>"
    b"<PhoneNumber>6882015026</PhoneNumber></ListOfPhoneNumbers>"
    b"<Triggered>false</Triggered><BillingType>PORTIN</BillingType>"
    b"</LnpOrderResponse>"
)

class ClassPortinsTest(TestCase):

    """Test port-in orders"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "baz", "qux")
        cls._account = Account(client=cls._client)
        cls._portins = cls._account.portins

    @classmethod
    def tearDownClass(cls):
        del cls._portins
        del cls._account
        del cls._client

    def test_get_loas(self):

        portin = self._portins.create({"order_id":
            "d28b36f7-fa96-49eb-9556-a40fca49f7c6"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + portin.loas.get_xpath()
            m.get(url, content=XML_RESPONSE_LOAS_GET)

            portin.loas.list({"metadata": "true"})

            self.assertEqual(portin.loas.result_message,
                "No LOA files found for order")

    def test_portin_activation_status_get(self):

        portin = self._portins.create({"order_id":
            "d28b36f7-fa96-49eb-9556-a40fca49f7c6"}, False)

        with requests_mock.Mocker() as m:

            url = portin.activation_status.get_xpath()
            m.get(url, content=XML_RESPONSE_ACTIVATION_STATUS)

            status = portin.activation_status.get()

            self.assertEqual(status.activated_telephone_numbers_list.\
                telephone_number.items[0], "6052609021")

    def test_portin_activation_status_set(self):

        portin = self._portins.create({"order_id":
            "d28b36f7-fa96-49eb-9556-a40fca49f7c6"}, False)

        portin.activation_status.auto_activation_status =\
            "2014-08-30T18:30:00+03:00"

        with requests_mock.Mocker() as m:

            url = portin.activation_status.get_xpath()
            m.put(url)

            status = portin.activation_status
            status.save()

    def test_portin_create(self):

        portin = self._portins.create({
            "billing_telephone_number": "6882015002",
            "subscriber": {
                "subscriber_type": "BUSINESS",
                "business_name": "Acme Corporation",
                "service_address": {
                    "house_number": "1623",
                    "street_name": "Brockton Ave",
                    "city": "Los Angeles",
                    "state_code": "CA",
                    "zip": "90025",
                    "country": "USA"
                }
            },
            "loa_authorizing_person": "John Doe",
            "list_of_phone_numbers": {
                "phone_number": ["9882015025", "9882015026"]
            },
            "site_id": "365",
            "triggered": "false"
        }, False)

        self.assertEqual(portin.list_of_phone_numbers.phone_number.items[1],
            "9882015026")
        self.assertEqual(portin.subscriber.service_address.street_name,
            "Brockton Ave")

        with requests_mock.Mocker() as m:

            url = self._portins.get_xpath()
            m.post(url, content=XML_RESPONSE_PORTIN_POST)

            portin = self._portins.create({
                "billing_telephone_number": "6882015002",
                "subscriber": {
                    "subscriber_type": "BUSINESS",
                    "business_name": "Acme Corporation",
                    "service_address": {
                        "house_number": "1623",
                        "street_name": "Brockton Ave",
                        "city": "Los Angeles",
                        "state_code": "CA",
                        "zip": "90025",
                        "country": "USA"
                    }
                },
                "loa_authorizing_person": "John Doe",
                "list_of_phone_numbers": {
                    "phone_number": ["9882015025", "9882015026"]
                },
                "site_id": "365",
                "triggered": "false"
            })

            self.assertEqual(portin.order_id,
                "d28b36f7-fa96-49eb-9556-a40fca49f7c6")

    def test_portin_delete(self):

        portin = self._portins.create({"order_id":
            "d28b36f7-fa96-49eb-9556-a40fca49f7c6"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + portin.get_xpath()
            m.delete(url)

            portin.delete()

    def test_portin_history(self):

        portin = self._portins.create({"order_id":
            "d28b36f7-fa96-49eb-9556-a40fca49f7c6"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + portin.history.get_xpath()
            m.get(url, content=XML_RESPONSE_HISTORY)

            history = portin.history.list()

            oh = history.items[0]
            self.assertEqual(len(history.items), 2)
            self.assertEqual(oh.order_date, "2015-06-03T15:06:35.765Z")
            self.assertEqual(oh.note, "LOA required")
            self.assertEqual(oh.author, "byo_dev")
            self.assertEqual(oh.status, "PENDING_DOCUMENTS")

    def test_portin_loas_delete(self):

        portin = self._portins.create({"order_id":
            "d28b36f7-fa96-49eb-9556-a40fca49f7c6"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + portin.loas.get_xpath() + "/fname"
            m.delete(url)

            portin.loas.delete("fname")

    def test_portin_loas_get_metadata(self):

        portin = self._portins.create({"order_id":
            "d28b36f7-fa96-49eb-9556-a40fca49f7c6"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + portin.loas.get_xpath() +\
                portin.loas.metadata._xpath.format("fname")
            m.get(url, content=XML_RESPONSE_META_GET)

            metadata = portin.loas.metadata.get("fname")

            self.assertEqual(metadata.document_name, "test.txt")
            self.assertEqual(metadata.document_type, "LOA")

    def test_portin_loas_set_metadata(self):

        portin = self._portins.create({"order_id":
            "d28b36f7-fa96-49eb-9556-a40fca49f7c6"}, False)

        portin.loas.metadata.id = "fname"
        portin.loas.metadata.document_name = "foo"
        portin.loas.metadata.document_type = "bar"

        with requests_mock.Mocker() as m:

            url = self._client.config.url +portin.loas.metadata.get_xpath()
            m.put(url)

            portin.loas.metadata.save()

    def test_portin_loas_delete_metadata(self):

        portin = self._portins.create({"order_id":
            "d28b36f7-fa96-49eb-9556-a40fca49f7c6"}, False)

        portin.loas.metadata.id = "fname"
        portin.loas.metadata.document_name = "foo"
        portin.loas.metadata.document_type = "bar"

        with requests_mock.Mocker() as m:

            url = self._client.config.url +portin.loas.metadata.get_xpath()
            m.delete(url)

            portin.loas.metadata.delete()

    def test_portin_update(self):

        portin = self._portins.create({
            "order_id": "d28b36f7-fa96-49eb-9556-a40fca49f7c6",
            "status": {
                "code": "0",
                "description": "empty"
            }
        }, False)
        portin.requested_foc_date = "2012-08-30T00:00:00.000Z"

        with requests_mock.Mocker() as m:

            url = self._client.config.url + portin.get_xpath()
            m.put(url, content=XML_RESPONSE_LNP_UPDATE)

            portin.save()

            self.assertEqual(portin.status.code, "200")
            self.assertEqual(portin.status.description,
                "Supp request received.")

if __name__ == "__main__":
    main()