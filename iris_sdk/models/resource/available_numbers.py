#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource

XML_NAME_AVAILABLE_NUMBERS = "TelephoneNumberList"
XPATH_AVAILABLE_NUMBERS = "/availableNumbers"

class AvailableNumbersData(object):

    @property
    def items(self):
        return self.telephone_number_list

    @property
    def telephone_number_list(self):
        return self._items

    @property
    def telephone_number(self):
        return self.telephone_number_list

class AvailableNumbers(AvailableNumbersData, BaseResource):

    """Available numbers for account"""

    _node_name = XML_NAME_AVAILABLE_NUMBERS
    _xpath = XPATH_AVAILABLE_NUMBERS

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)
        self._items = []

    def list(self, params=None):
        self.get_data(params=params, node_name=self._node_name)
        return self.items