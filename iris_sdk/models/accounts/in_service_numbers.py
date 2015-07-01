#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.accounts.in_service_numbers_tn import Tn
from iris_sdk.models.accounts.in_service_numbers_totals import Totals
from iris_sdk.models.base_resource import BaseResource, BaseResourceSimpleList
from iris_sdk.models.data.links import Links
from iris_sdk.models.data.telephone_number import TelephoneNumber

XML_NAME_IN_SERVICE_NUMBERS = "TNs"
XPATH_IN_SERVICE_NUMBERS = "/inserviceNumbers"

class InserviceNumbersData(object):

    @property
    def links(self):
        return self._links

    @property
    def result_count(self):
        return self.total_count

    @property
    def telephone_numbers(self):
        return self._telephone_numbers

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
        self._links = Links()
        self._telephone_numbers = BaseResourceSimpleList(TelephoneNumber)
        self._tn = Tn(client, self._xpath)
        self._total_count = None
        self._totals = Totals(client, self._xpath)

    def clear(self):
        self.links.clear()
        self.telephone_numbers.clear()
        self.total_count = None
        self.totals.clear()

    def list(self, params=None):
        self.clear()
        self.get_data(params=params)
        return self.telephone_numbers

    def totals_count(self):
        self.totals.get()
        return self.totals.count

    def verify(self, number):
        return self.tn.get(number)