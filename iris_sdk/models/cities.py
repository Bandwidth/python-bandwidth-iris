#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.cities import CitiesData

XML_NAME_CITIES = "CityResponse"
XPATH_RATE_CITIES = "/cities"

class Cities(BaseResource, CitiesData):

    """Covered cities directory"""

    _node_name = XML_NAME_CITIES
    _xpath = XPATH_RATE_CITIES

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        CitiesData.__init__(self)

    def list(self, params):
        return self._get_data(params=params).cities.city