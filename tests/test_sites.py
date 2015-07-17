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

XML_RESPONSE_PORTINS_LIST = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<LNPResponseWrapper><TotalCount>4</TotalCount><Links>"
    b"<first></first></Links><lnpPortInfoForGivenStatus>"
    b"<CountOfTNs>1</CountOfTNs><userId>System</userId>"
    b"<lastModifiedDate>2015-06-03T15:06:36.234Z</lastModifiedDate>"
    b"<OrderDate>2015-06-03T15:06:35.533Z</OrderDate>"
    b"<OrderId>535ba91e-5363-474e-8c97-c374a4aa6a02</OrderId>"
    b"<OrderType>port_in</OrderType>"
    b"<BillingTelephoneNumber>9193491234</BillingTelephoneNumber>"
    b"<LNPLosingCarrierId>1537</LNPLosingCarrierId>"
    b"<LNPLosingCarrierName>Test Losing Carrier L3</LNPLosingCarrierName>"
    b"<ProcessingStatus>SUBMITTED</ProcessingStatus>"
    b"<RequestedFOCDate>2015-06-03T15:30:00.000Z</RequestedFOCDate>"
    b"<VendorId>49</VendorId><VendorName>Bandwidth CLEC</VendorName>"
    b"<PON>BWC1433343996123</PON></lnpPortInfoForGivenStatus>"
    b"<lnpPortInfoForGivenStatus><CountOfTNs>1</CountOfTNs>"
    b"<userId>byo_dev</userId>"
    b"<lastModifiedDate>2015-06-03T15:10:13.384Z</lastModifiedDate>"
    b"<OrderDate>2015-06-03T15:10:12.808Z</OrderDate>"
    b"<OrderId>98939562-90b0-40e9-8335-5526432d9741</OrderId>"
    b"<OrderType>port_in</OrderType>"
    b"<BillingTelephoneNumber>7576768750</BillingTelephoneNumber>"
    b"<LNPLosingCarrierId>1537</LNPLosingCarrierId>"
    b"<LNPLosingCarrierName>Test Losing Carrier L3</LNPLosingCarrierName>"
    b"<ProcessingStatus>SUBMITTED</ProcessingStatus>"
    b"<RequestedFOCDate>2015-06-03T15:30:00.000Z</RequestedFOCDate>"
    b"<VendorId>49</VendorId><VendorName>Bandwidth CLEC</VendorName>"
    b"<PON>BWC1433344213212</PON></lnpPortInfoForGivenStatus>"
    b"</LNPResponseWrapper>"
)

XML_RESPONSE_SITES_LIST = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<SitesResponse><Sites><Site><Id>2297</Id><Name>API Test Site</Name>"
    b"</Site><Site><Id>2301</Id><Name>My First Site</Name>"
    b"<Description>A Site From Node SDK Examples</Description></Site>"
    b"</Sites></SitesResponse>"
)

XML_RESPONSE_TOTAL_TNS = (
   b"<SiteTNsResponse><SiteTNs><TotalCount>60</TotalCount></SiteTNs>"
   b"</SiteTNsResponse>"
)

class ClassSitesTest(TestCase):

    """Test sites"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._client
        del cls._account

    def test_portins_get(self):

        site = self._account.sites.create({"id": "1337"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + site.portins.get_xpath()
            m.get(url, content=XML_RESPONSE_PORTINS_LIST)

            portins = site.portins.list({"page": 1, "size": 10})
            pi = portins.items[0]

            self.assertEqual(len(portins.items), 2)
            self.assertEqual(pi.count_of_tns, "1")
            self.assertEqual(pi.last_modified_date,"2015-06-03T15:06:36.234Z")
            self.assertEqual(pi.order_date, "2015-06-03T15:06:35.533Z")
            self.assertEqual(pi.order_type, "port_in")
            self.assertEqual(pi.lnp_losing_carrier_id, "1537")
            self.assertEqual(pi.lnp_losing_carrier_name,
                "Test Losing Carrier L3")
            self.assertEqual(pi.requested_foc_date,"2015-06-03T15:30:00.000Z")
            self.assertEqual(pi.vendor_id, "49")
            self.assertEqual(pi.vendor_name, "Bandwidth CLEC")
            self.assertEqual(pi.pon, "BWC1433343996123")
            self.assertEqual(pi.order_id,
                "535ba91e-5363-474e-8c97-c374a4aa6a02")
            self.assertEqual(pi.processing_status, "SUBMITTED")

    def test_site_create(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._account.sites.get_xpath()
            m.post(url, headers={"location": ".../2489"})

            site = self._account.sites.create({
                "name": "Foo",
                "address": {
                    "city": "Raleigh"
                }
            })

            self.assertEqual(site.id, "2489")
            self.assertEqual(site.name, "Foo")
            self.assertEqual(site.address.city, "Raleigh")

    def test_site_delete(self):

        site = self._account.sites.create({"id": "1337"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + site.get_xpath()
            m.delete(url)

            site.delete()

    def test_site_orders(self):

        orders = self._account.sites.create({"id": "1337"}, False).orders

        with requests_mock.Mocker() as m:

            url = self._client.config.url + orders.get_xpath()
            m.get(url)

            orders_list = orders.list({"page": 1, "size": 5})

    def test_site_orders_tns(self):

        site = self._account.sites.create({"id": "1337"}, False)
        order = site.orders.create({"order_id": "1"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + order.tns.get_xpath()
            m.get(url)

            order.tns.list()

    def test_site_total_tns(self):

        site = self._account.sites.create({"id": "1337"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + site.totaltns.get_xpath()
            m.get(url, content=XML_RESPONSE_TOTAL_TNS)

            cnt = site.totaltns.get().total_count

            self.assertEqual(cnt, "60")

    def test_site_update(self):

        site = self._account.sites.create({"id": "1337"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + site.get_xpath()
            m.put(url)

            site.save()

    def test_sites_list(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._account.sites.get_xpath()
            m.get(url, content=XML_RESPONSE_SITES_LIST)

            sites = self._account.sites.list()

            self.assertEqual(len(sites.items), 2)
            self.assertEqual(sites.items[0].id, "2297")

if __name__ == "__main__":
    main()