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
from iris_sdk.models.covered_rate_centers import CoveredRateCenters
from iris_sdk.models.rate_center import RateCenter

XML_RESPONSE_CRC_GET = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?> "
    "<CoveredRateCenters><CoveredRateCenter><Name>AVALON</Name>"
    "<Abbreviation>AVALON</Abbreviation> <State>CA</State><Lata>730</Lata> "
    "<AvailableNumberCount>1</AvailableNumberCount> <ZipCodes>"
    "<ZipCode>90731</ZipCode> </ZipCodes><Cities><City>SAN PEDRO</City> "
    "</Cities><Tiers> <Tier>0</Tier></Tiers> <NpaNxxXs>"
    "<NpaNxxX>3105100</NpaNxxX> <NpaNxxX>3105101</NpaNxxX> "
    "<NpaNxxX>3109498</NpaNxxX> <NpaNxxX>3109499</NpaNxxX> "
    "<NpaNxxX>4242260</NpaNxxX></NpaNxxXs><Id>1</Id> "
    "</CoveredRateCenter></CoveredRateCenters>"
)

XML_RESPONSE_CRC_LIST_GET = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<CoveredRateCenters><TotalCount>18</TotalCount> <Links>"
    "<first>Link=&lt;https://api.inetwork.com:443/v1.0/coveredRateCenters?"
    "npa=310&amp;size=10&amp;e mbed=Cities&amp;embed=ZipCodes&amp;embed="
    "NpaNxxX&amp;page=1&gt;;rel=\"first\";</first><next>Link=&lt;"
    "https://api.inetwork.com:443/v1.0/coveredRateCenters?npa=310&amp;"
    "size=10&amp;e mbed=Cities&amp;embed=ZipCodes&amp;embed=NpaNxxX&amp; "
    "page=5&gt;;rel=\"next\";</next></Links> <CoveredRateCenter>"
    "<Name>AVALON</Name><Abbreviation>AVALON</Abbreviation> "
    "<State>CA</State><Lata>730</Lata> "
    "<AvailableNumberCount>1</AvailableNumberCount> <ZipCodes>"
    "<ZipCode>90731</ZipCode> </ZipCodes><Cities><City>SAN PEDRO</City> "
    "</Cities><Tiers> <Tier>0</Tier></Tiers> <NpaNxxXs>"
    "<NpaNxxX>3105100</NpaNxxX> <NpaNxxX>3105101</NpaNxxX> "
    "<NpaNxxX>3109498</NpaNxxX> <NpaNxxX>3109499</NpaNxxX> "
    "<NpaNxxX>4242260</NpaNxxX></NpaNxxXs><Id>1</Id> "
    "</CoveredRateCenter> <CoveredRateCenter><Name>BEVERLY HILLS</Name> "
    "<Abbreviation>BEVERLYHLS</Abbreviation> <State>CA</State>"
    "<Lata>730</Lata><AvailableNumberCount>25</AvailableNumberCount> "
    "<ZipCodes><ZipCode>90013</ZipCode> <ZipCode>90014</ZipCode> "
    "<ZipCode>90015</ZipCode><ZipCode>91504</ZipCode>"
    "<ZipCode>91505</ZipCode> </ZipCodes><Cities>"
    "<City>BEVERLY HILLS</City> <City>BURBANK</City> <City>GARDENA</City> "
    "<City>LOS ANGELES</City> <City>SHERMAN OAKS</City> "
    "<City>SUN VALLEY</City> <City>VAN NUYS</City></Cities> "
    "<Tiers><Tier>0</Tier> </Tiers><NpaNxxXs> <NpaNxxX>3102010</NpaNxxX>"
    "<NpaNxxX>3102011</NpaNxxX><NpaNxxX>3102012</NpaNxxX>"
    "<NpaNxxX>4247777</NpaNxxX> <NpaNxxX>4247778</NpaNxxX> "
    "<NpaNxxX>4247779</NpaNxxX></NpaNxxXs><Id>3</Id> "
    "</CoveredRateCenter></CoveredRateCenters>"
)

class ClassCoveredRateCentersTest(TestCase):

    """Test the covered rate centers directory mapping"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._crc = CoveredRateCenters(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._client
        del cls._crc

    def test_rate_center_get(self):
        url = self._crc.client.config.url +\
            self._crc.get_xpath() + RateCenter._xpath.format("1")
        with requests_mock.Mocker() as m:
            m.get(url, content=XML_RESPONSE_CRC_GET)
            center = self._crc.get(1)
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(center.name, "AVALON")
            self.assertEquals(center.abbreviation, "AVALON")
            self.assertEquals(center.state, "CA")
            self.assertEquals(center.lata, "730")
            self.assertEquals(center.available_number_count, "1")
            self.assertEquals(center.zip_codes.zip_code.items[0], "90731")
            self.assertEquals(center.cities.city.items[0], "SAN PEDRO")
            self.assertEquals(center.tiers.tier.items[0], "0")
            self.assertEquals(center.npa_nxx_xs.npa_nxx_x.items,
                ["3105100","3105101","3109498","3109499","4242260"])

    def test_rate_centers_list(self):
        self.assertEquals(self._crc.get_xpath(), self._crc._xpath)
        with requests_mock.Mocker() as m:
            m.get(self._crc.client.config.url + self._crc.get_xpath(),
                content=XML_RESPONSE_CRC_LIST_GET)
            centers = self._crc.list({"page": 1, "size": 2})
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(len(centers.items), 2)
            item = centers.items[0]
            self.assertEquals(item.name, "AVALON")
            self.assertEquals(item.abbreviation, "AVALON")
            self.assertEquals(item.state, "CA")
            self.assertEquals(item.lata, "730")
            self.assertEquals(item.available_number_count, "1")
            self.assertEquals(item.zip_codes.zip_code.items[0], "90731")
            self.assertEquals(item.cities.city.items[0], "SAN PEDRO")
            self.assertEquals(item.tiers.tier.items[0], "0")
            self.assertEquals(item.npa_nxx_xs.npa_nxx_x.items,
                ["3105100","3105101","3109498","3109499","4242260"])
            self.assertEquals(item.id, "1")

if __name__ == "__main__":
    main()