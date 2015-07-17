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
from iris_sdk.models.cities import Cities

XML_RESPONSE_CITIES_LIST = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<CityResponse><ResultCount>618</ResultCount><Cities><City>"
    "<RcAbbreviation>PINEHURST</RcAbbreviation><Name>ABERDEEN</Name></City>"
    "<City><RcAbbreviation>JULIAN</RcAbbreviation><Name>ADVANCE</Name>"
    "</City></Cities></CityResponse>"
)

class ClassCitiesTest(TestCase):

    """Test the Cities dir"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._cities = Cities(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._cities
        del cls._client

    def test_cities_list(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._cities.get_xpath()
            m.get(url, content=XML_RESPONSE_CITIES_LIST)
            
            city = self._cities.list({"state": "NC"}).items[0]

            self.assertEqual(city.rc_abbreviation, "PINEHURST")
            self.assertEqual(city.name, "ABERDEEN")

if __name__ == "__main__":
    main()