#!/usr/bin/env python

#from abc import ABC

from iris_sdk.models.resource import BaseResource

XML_NAME_AVAILABLE_NUMBERS = "TelephoneNumberList"
XPATH_AVAILABLE_NUMBERS = "/availableNumbers"

class AvailableNumbersData():

    @property
    def items(self):
        return self._items

    @property
    def telephone_number(self):
        return self.items

class AvailableNumbers(AvailableNumbersData, BaseResource):

    """Available numbers for account"""

    _node_name = XML_NAME_AVAILABLE_NUMBERS
    _xpath = XPATH_AVAILABLE_NUMBERS

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)
        self._items = []

    def list(self, params=None):
        super().get_raw(params=params, node_name=self._node_name)
        return self.items