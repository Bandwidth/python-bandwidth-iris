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
from iris_sdk.models.rate_centers import RateCenters

XML_RESPONSE_RC_LIST = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<RateCenterResponse><ResultCount>652</ResultCount><RateCenters>"
    "<RateCenter><Abbreviation>AGOURA</Abbreviation><Name>AGOURA</Name>"
    "</RateCenter><RateCenter><Abbreviation>ALAMITOS</Abbreviation>"
    "<Name>ALAMITOS</Name></RateCenter></RateCenters></RateCenterResponse>"
)

class ClassRcTest(TestCase):

    """Test the Rate centers dir"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._rc = RateCenters(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._rc
        del cls._client

    def test_rc_list(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._rc.get_xpath()
            m.get(url, content=XML_RESPONSE_RC_LIST)
            
            rc = self._rc.list({"state": "CA"}).items[0]

            self.assertEqual(rc.name, "AGOURA")
            self.assertEqual(rc.abbreviation, "AGOURA")

if __name__ == "__main__":
    main()