#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.totals import Totals
from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.in_service_numbers import InServiceNumbersData

XML_NAME_IN_SERVICE_NUMBERS = "TNs"
XPATH_IN_SERVICE_NUMBERS = "/inserviceNumbers"

class InServiceNumbers(BaseResource, InServiceNumbersData):

    """In-service numbers for account"""

    _node_name = XML_NAME_IN_SERVICE_NUMBERS
    _xpath = XPATH_IN_SERVICE_NUMBERS

    @property
    def totals(self):
        return self._totals

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        InServiceNumbersData.__init__(self)
        self._totals = Totals(self, client)

    def list(self, params=None):
        self.get_data(params=params)
        return self.telephone_numbers

    def totals_count(self):
        self.totals.get()
        return self.totals.count