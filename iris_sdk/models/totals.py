#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.maps.totals import TotalsMap

XML_NAME_IN_SERVICE_NUMBERS_TOTALS = "Quantity"
XPATH_IN_SERVICE_NUMBERS_TOTALS = "/totals"

class Totals(TotalsMap, BaseResource):

    """In-service numbers totals for account"""

    _node_name = XML_NAME_IN_SERVICE_NUMBERS_TOTALS
    _xpath = XPATH_IN_SERVICE_NUMBERS_TOTALS

    def get(self):
        return self.get_data()