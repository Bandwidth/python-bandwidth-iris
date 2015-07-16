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
    b"<CoveredRateCenter>"
    b"    <Name>LOMITA</Name>"
    b"    <Abbreviation>LOMITA</Abbreviation>"
    b"    <State>CA</State>"
    b"    <Lata>730</Lata>"
    b"    <AvailableNumberCount>5536</AvailableNumberCount>"
    b"    <ZipCodes>"
    b"        <ZipCode>90044</ZipCode>"
    b"        <ZipCode>90059</ZipCode>"
    b"        <ZipCode>90061</ZipCode>"
    b"        <ZipCode>90247</ZipCode>"
    b"        <ZipCode>90248</ZipCode>"
    b"        <ZipCode>90249</ZipCode>"
    b"        <ZipCode>90717</ZipCode>"
    b"        <ZipCode>90802</ZipCode>"
    b"        <ZipCode>90813</ZipCode>"
    b"        <ZipCode>90822</ZipCode>"
    b"        <ZipCode>90831</ZipCode>"
    b"        <ZipCode>90834</ZipCode>"
    b"    </ZipCodes>"
    b"    <Cities>"
    b"        <City>GARDENA</City>"
    b"        <City>LOMITA</City>"
    b"        <City>LONG BEACH</City>"
    b"        <City>LOS ANGELES</City>"
    b"    </Cities>"
    b"    <Tiers>"
    b"        <Tier>0</Tier>"
    b"    </Tiers>"
    b"    <NpaNxxXs>"
    b"        <NpaNxxX>3102570</NpaNxxX>"
    b"        <NpaNxxX>3102571</NpaNxxX>"
    b"    </NpaNxxXs>"
    b"    <Id>1</Id>"
    b"    <LocalRateCenters>"
    b"        <RateCenterId>369</RateCenterId>"
    b"        <RateCenterId>7843</RateCenterId>"
    b"        <RateCenterId>7945</RateCenterId>"
    b"    </LocalRateCenters>"
    b"</CoveredRateCenter>"
)

XML_RESPONSE_CRC_LIST_GET = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<CoveredRateCenters>"
    b"    <Links>"
    b"        <first></first>"
    b"    </Links>"
    b"    <CoveredRateCenter>"
    b"        <Id>2805</Id>"
    b"        <Name>CARY</Name>"
    b"        <Abbreviation>CARY</Abbreviation>"
    b"        <State>NC</State>"
    b"        <Lata>426</Lata>"
    b"        <Tiers>"
    b"            <Tier>0</Tier>"
    b"        </Tiers>"
    b"    </CoveredRateCenter>"
    b"    <CoveredRateCenter>"
    b"        <Id>2807</Id>"
    b"        <Name>CARY-RESEARCH TRIANGLE PARK</Name>"
    b"        <Abbreviation>CARY-RTP</Abbreviation>"
    b"        <State>NC</State>"
    b"        <Lata>426</Lata>"
    b"        <Tiers>"
    b"            <Tier>0</Tier>"
    b"        </Tiers>"
    b"    </CoveredRateCenter>"
    b"</CoveredRateCenters>"
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
            self.assertEquals(center.lata, "730")
            self.assertEquals(center.cities.city.items[2], "LONG BEACH")

    def test_rate_centers_list(self):
        self.assertEquals(self._crc.get_xpath(), self._crc._xpath)
        with requests_mock.Mocker() as m:
            m.get(self._crc.client.config.url + self._crc.get_xpath(),
                content=XML_RESPONSE_CRC_LIST_GET)
            centers = self._crc.list({"page": 1, "size": 2})
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(len(centers.items), 2)
            self.assertEquals(centers.items[0].tiers.tier.items[0], "0")

if __name__ == "__main__":
    main()