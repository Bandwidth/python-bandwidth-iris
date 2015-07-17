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
from iris_sdk.models.tns import Tns

XML_RESPONSE_LCA_GET = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<SearchResult><ListofNPANXX><NPANXX>240206</NPANXX>"
    "<NPANXX>240228</NPANXX></ListofNPANXX><Location><RateCenters>"
    "<State>MD</State><RCs><RC>MILLERSVL</RC><RC>SEVERNA PK</RC></RCs>"
    "</RateCenters></Location></SearchResult>"
)

XML_RESPONSE_TN_GET = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<TelephoneNumberResponse><TelephoneNumber>7576768750</TelephoneNumber>"
    "<Status>PortInPendingFoc</Status>"
    "<LastModifiedDate>2015-06-03T15:10:13.000Z</LastModifiedDate>"
    "<OrderCreateDate>2015-06-03T15:10:12.808Z</OrderCreateDate>"
    "<OrderId>98939562-90b0-40e9</OrderId>"
    "<OrderType>PORT_NUMBER_ORDER</OrderType>"
    "<SiteId>2297</SiteId>"
    "<AccountId>9500249</AccountId></TelephoneNumberResponse>"
)

XML_RESPONSE_TN_HISTORY_GET = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<TelephoneNumberResponse><TelephoneNumberStatuses>"
    "<TelephoneNumberStatus><AccountId>753</AccountId>"
    "<LastModifiedDate>2014-07-29T13:42:49.789Z</LastModifiedDate>"
    "<OrderCreateDate>2014-07-29T13:42:33.000Z</OrderCreateDate>"
    "<OrderId>58ee5da9-6357-4626-86fd-6faf4bf819b3</OrderId>"
    "<Status>Available</Status><UserId>jbm</UserId>"
    "<OrderType>IMPORT_AVAILABLE_ORDER</OrderType></TelephoneNumberStatus>"
    "<TelephoneNumberStatus><AccountId>14</AccountId>"
    "<LastModifiedDate>2014-07-30T11:07:10.585Z</LastModifiedDate>"
    "<OrderCreateDate>2014-07-30T11:07:10.537Z</OrderCreateDate>"
    "<OrderId>90d7f38d-03fc-43f4-85f6-ed2608411775</OrderId>"
    "<Status>Inservice</Status><UserId>jbm</UserId>"
    "<OrderType>NEW_NUMBER_ORDER</OrderType></TelephoneNumberStatus>"
    "</TelephoneNumberStatuses></TelephoneNumberResponse>"
)

XML_RESPONSE_TN_LIST = (
    "<TelephoneNumbersResponse>"
    "<TelephoneNumberCount>78</TelephoneNumberCount><Links><first></first>"
    "<next></next></Links><TelephoneNumbers><TelephoneNumber>"
    "<City>MILLERSVILLE</City><Lata>238</Lata><State>MD</State>"
    "<FullNumber>4109235436</FullNumber><Tier>0</Tier><VendorId>49</VendorId>"
    "<VendorName>Bandwidth CLEC</VendorName>"
    "<RateCenter>MILLERSVL</RateCenter><Status>PortInPendingFoc</Status>"
    "<AccountId>9500249</AccountId>"
    "<LastModified>2015-07-14T13:53:58.000Z</LastModified></TelephoneNumber>"
    "<TelephoneNumber><City>MILLERSVILLE</City><Lata>238</Lata>"
    "<State>MD</State><FullNumber>4109235437</FullNumber><Tier>0</Tier>"
    "<VendorId>49</VendorId><VendorName>Bandwidth CLEC</VendorName>"
    "<RateCenter>MILLERSVL</RateCenter><Status>PortInPendingFoc</Status>"
    "<AccountId>9500249</AccountId>"
    "<LastModified>2015-07-14T19:13:57.000Z</LastModified></TelephoneNumber>"
    "</TelephoneNumbers></TelephoneNumbersResponse>"
)

XML_RESPONSE_SIP_PEER_GET = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><SipPeer>"
    "<Id>500651</Id><Name>Something</Name></SipPeer>"
)

XML_RESPONSE_SITE_GET = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><Site>"
    "<Id>2297</Id><Name>API Test Site</Name></Site>"
)

XML_RESPONSE_TN_LATA_GET = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<TelephoneNumberResponse><TelephoneNumberDetails><Lata>252</Lata>"
    "</TelephoneNumberDetails></TelephoneNumberResponse>"
)

XML_RESPONSE_TN_RC_GET = (
   "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
   "<TelephoneNumberResponse><TelephoneNumberDetails><State>VA</State>"
   "<RateCenter>NRFOLKZON1</RateCenter></TelephoneNumberDetails>"
   "</TelephoneNumberResponse>"
)

XML_RESPONSE_TNDETAILS_GET = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<TelephoneNumberResponse><TelephoneNumberDetails>"
    "<City>JERSEY CITY</City><Lata>224</Lata><State>NJ</State>"
    "<FullNumber>2018981023</FullNumber><Tier>0</Tier>"
    "<VendorId>49</VendorId><VendorName>Bandwidth CLEC</VendorName>"
    "<RateCenter>JERSEYCITY</RateCenter><Status>Inservice</Status>"
    "<AccountId>14</AccountId>"
    "<LastModified>2014-07-30T11:29:37.000Z</LastModified><Features>"
    "<E911><Status>Success</Status></E911><Lidb>"
    "<Status>Pending</Status>"
    "<SubscriberInformation>Fred</SubscriberInformation>"
    "<UseType>BUSINESS</UseType><Visibility>PUBLIC</Visibility>"
    "</Lidb><Dlda><Status>Success</Status>"
    "<SubscriberType>BUSINESS</SubscriberType>"
    "<ListingType>LISTED</ListingType><ListingName>"
    "<FirstName>Joe</FirstName><LastName>Smith</LastName>"
    "</ListingName><ListAddress>true</ListAddress><Address>"
    "<HouseNumber>12</HouseNumber><StreetName>ELM</StreetName>"
    "<City>New York</City><StateCode>NY</StateCode><Zip>10007</Zip>"
    "<Country>United States</Country><AddressType>Dlda</AddressType>"
    "</Address></Dlda></Features><TnAttributes>"
    "<TnAttribute>Protected</TnAttribute></TnAttributes>"
    "</TelephoneNumberDetails></TelephoneNumberResponse>"
)

XML_RESPONSE_TNRESERVATION_GET = (
   "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
   "<TNReservation><ReservationId>123</ReservationId>"
   "<AccountId>111</AccountId><ReservationExpires>0</ReservationExpires>"
   "<ReservedTn>6136211234</ReservedTn></TNReservation>"
)

class ClassTnsTest(TestCase):

    """Telephone number tests"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)
        cls._tns = Tns(client=cls._client)
        cls._url = cls._client.config.url +cls._tns.get_xpath() +"/7576768750"

    @classmethod
    def tearDownClass(cls):
        del cls._account
        del cls._tns
        del cls._client

    def test_history(self):

        with requests_mock.Mocker() as m:

            m.get(self._url, content=XML_RESPONSE_TN_GET)

            tn = self._tns.get("7576768750")

            url = self._client.config.url + tn.history.get_xpath()
            m.get(url, content=XML_RESPONSE_TN_HISTORY_GET)

            hs = tn.history.list().items[0]

            self.assertEqual(hs.account_id, "753")
            self.assertEqual(hs.last_modified_date,
                "2014-07-29T13:42:49.789Z")
            self.assertEqual(hs.order_create_date,
                "2014-07-29T13:42:33.000Z")
            self.assertEqual(hs.order_id,
                "58ee5da9-6357-4626-86fd-6faf4bf819b3")
            self.assertEqual(hs.order_type, "IMPORT_AVAILABLE_ORDER")
            self.assertEqual(hs.status, "Available")

    def test_lca(self):

        with requests_mock.Mocker() as m:

            m.get(self._url, content=XML_RESPONSE_TN_GET)

            tn = self._tns.get("7576768750")

            url = self._client.config.url + tn.lca.get_xpath()
            m.get(url, content=XML_RESPONSE_LCA_GET)

            lca = tn.lca.get()

            self.assertEqual(lca.listof_npanxx.npanxx.items[0], "240206")
            self.assertEqual(lca.listof_npanxx.npanxx.items[1], "240228")
            self.assertEqual(
                lca.location.rate_centers.items[0].state, "MD")
            self.assertEqual(
                lca.location.rate_centers.items[0].rcs.rc.items[0],
                "MILLERSVL")
            self.assertEqual(
                lca.location.rate_centers.items[0].rcs.rc.items[1],
                "SEVERNA PK")

    def test_sip_peer(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url+self._tns.get_xpath()+"/7576768750"
            m.get(url, content=XML_RESPONSE_TN_GET)

            tn = self._tns.get("7576768750")

            url = self._client.config.url + tn.sip_peer.get_xpath()
            m.get(url, content=XML_RESPONSE_SIP_PEER_GET)

            sip_peer = tn.sip_peer.get()

            self.assertEqual(sip_peer.id, "500651")
            self.assertEqual(sip_peer.peer_name, "Something")

    def test_site(self):

        with requests_mock.Mocker() as m:

            m.get(self._url, content=XML_RESPONSE_TN_GET)

            tn = self._tns.get("7576768750")

            url = self._client.config.url + tn.site.get_xpath()
            m.get(url, content=XML_RESPONSE_SITE_GET)

            site = tn.site.get()

            self.assertEqual(site.id, "2297")
            self.assertEqual(site.name, "API Test Site")

    def test_tn(self):

        with requests_mock.Mocker() as m:

            m.get(self._url, content=XML_RESPONSE_TN_GET)

            tn = self._tns.get("7576768750")

            self.assertEqual(tn.status, "PortInPendingFoc")
            self.assertEqual(tn.order_id, "98939562-90b0-40e9")

    def test_tn_lata(self):

        with requests_mock.Mocker() as m:

            m.get(self._url, content=XML_RESPONSE_TN_GET)

            tn = self._tns.get("7576768750")

            url = self._client.config.url + tn.tn_lata.get_xpath()
            m.get(url, content=XML_RESPONSE_TN_LATA_GET)

            lata = tn.tn_lata.get()

            self.assertEqual(lata.lata, "252")

    def test_tn_list(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._tns.get_xpath()
            m.get(url, content=XML_RESPONSE_TN_LIST)
            
            tns = self._tns.list({"page": 1, "size": 10})

            self.assertEqual(len(tns.items), 2)
            self.assertEqual(tns.items[0].full_number, "4109235436")

    def test_tn_rate_center(self):

        with requests_mock.Mocker() as m:

            m.get(self._url, content=XML_RESPONSE_TN_GET)

            tn = self._tns.get("7576768750")

            url = self._client.config.url + tn.tn_rate_center.get_xpath()
            m.get(url, content=XML_RESPONSE_TN_RC_GET)

            rc = tn.tn_rate_center.get()

            self.assertEqual(rc.rate_center, "NRFOLKZON1")
            self.assertEqual(rc.state, "VA")

    def test_tndetails(self):

        with requests_mock.Mocker() as m:

            m.get(self._url, content=XML_RESPONSE_TN_GET)

            tn = self._tns.get("7576768750")

            url = self._client.config.url + tn.tndetails.get_xpath()
            m.get(url, content=XML_RESPONSE_TNDETAILS_GET)

            tnd = tn.tndetails.get()

            self.assertEqual(tnd.city, "JERSEY CITY")
            self.assertEqual(tnd.lata, "224")
            self.assertEqual(tnd.state, "NJ")
            self.assertEqual(tnd.full_number, "2018981023")
            self.assertEqual(tnd.tier, "0")
            self.assertEqual(tnd.vendor_id, "49")
            self.assertEqual(tnd.vendor_name, "Bandwidth CLEC")
            self.assertEqual(tnd.rate_center, "JERSEYCITY")
            self.assertEqual(tnd.status, "Inservice")
            self.assertEqual(tnd.account_id, "14")
            self.assertEqual(tnd.last_modified, "2014-07-30T11:29:37.000Z")
            self.assertEqual(tnd.features.lidb.status, "Pending")

    def test_tnreservation(self):

        with requests_mock.Mocker() as m:

            m.get(self._url, content=XML_RESPONSE_TN_GET)

            tn = self._tns.get("7576768750")

            url = self._client.config.url + tn.tnreservation.get_xpath()
            m.get(url, content=XML_RESPONSE_TNRESERVATION_GET)

            tnr = tn.tnreservation.get()

            self.assertEqual(tnr.id, "123")
            self.assertEqual(tnr.reserved_tn, "6136211234")
            self.assertEqual(tnr.reservation_expires, "0")
            self.assertEqual(tnr.account_id, "111")

if __name__ == "__main__":
    main()