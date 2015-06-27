#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource

XML_NAME_IN_SERVICE_NUMBERS_TOTALS = "Quantity"
XPATH_IN_SERVICE_NUMBERS_TOTALS = "/totals"

class TotalsData(object):

    @property
    def count(self):
        return self._count
    @count.setter
    def count(self, count):
        self._count = count

class Totals(TotalsData, BaseResource):

    """In-service numbers totals for account"""

    _node_name = XML_NAME_IN_SERVICE_NUMBERS_TOTALS
    _xpath = XPATH_IN_SERVICE_NUMBERS_TOTALS

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)
        self._count = None

    def get(self):
        return self.get_data(node_name=self._node_name)