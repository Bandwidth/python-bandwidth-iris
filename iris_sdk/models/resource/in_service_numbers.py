#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.resource.data.in_service_numbers.tn import TN
from iris_sdk.models.resource.data.in_service_numbers.totals import Totals
from iris_sdk.models.base_resource import BaseResource

XML_NAME_IN_SERVICE_NUMBERS = "TNs"
XPATH_IN_SERVICE_NUMBERS = "/inserviceNumbers"

class InserviceNumbersData(object):

    @property
    def items(self):
        return self.telephone_numbers

    @property
    def telephone_numbers(self):
        return self._items

    @property
    def telephone_number(self):
        return self.telephone_numbers

    @property
    def tn(self):
        return self._tn

    @property
    def total_count(self):
        return self._total_count
    @total_count.setter
    def total_count(self, total_count):
        self._total_count = total_count

    @property
    def totals(self):
        return self._totals

class InserviceNumbers(InserviceNumbersData, BaseResource):

    """In-service numbers for account"""

    _node_name = XML_NAME_IN_SERVICE_NUMBERS
    _xpath = XPATH_IN_SERVICE_NUMBERS

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)
        self._total_count = None
        self._items = []
        self._totals = Totals(client, self._xpath)
        self._tn = TN(client, self._xpath)

    def list(self, params=None):
        self.get_data(params, node_name=self._node_name)
        self.telephone_numbers.pop(0)
        return self.items

    def totals_count(self):
        self.totals.get()
        return self.totals.count

    def verify(self, number):
        return self.tn.get(number)