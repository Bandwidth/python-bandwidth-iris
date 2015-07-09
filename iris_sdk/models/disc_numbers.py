#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.include.xml_consts import XML_PARAM_TN_DETAIL, XML_TRUE
from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.disc_numbers import DiscNumbersData
from iris_sdk.models.totals import Totals

XML_NAME_DISC_NUMBERS = "TNs"
XPATH_DISC_NUMBERS = "/discnumbers"

class DiscNumbers(BaseResource, DiscNumbersData):

    """Disconnected numbers for account"""

    _node_name = XML_NAME_DISC_NUMBERS
    _xpath = XPATH_DISC_NUMBERS

    @property
    def totals(self):
        return self._totals

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        DiscNumbersData.__init__(self)
        self._totals = Totals(self)

    def list(self, params):
        return self._get_data(params=params).telephone_number_list

    def totals_count(self):
        self.totals.get()
        return self.totals.count