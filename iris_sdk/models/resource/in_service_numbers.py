#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.resource.data.in_service_numbers.tn import TN
from iris_sdk.models.resource.data.in_service_numbers.totals import Totals

XML_NAME_IN_SERVICE_NUMBERS = "TNs"
XPATH_IN_SERVICE_NUMBERS = "/inserviceNumbers"

class InserviceNumbersData(object):

    @property
    def items(self):
        return self.telephone_numbers

    @property
    def search_count(self):
        return self.total_count

    @property
    def telephone_numbers(self):
        return self._items

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

    def clear(self):
        del self.telephone_numbers[:]
        self._total_count = None

    def list(self, params=None):
        self.clear()
        self.get_data(params=params)
        self._prepare_list(self.telephone_numbers)
        return self.telephone_numbers

    def totals_count(self):
        self.totals.get()
        return self.totals.count

    def verify(self, number):
        return self.tn.get(number)