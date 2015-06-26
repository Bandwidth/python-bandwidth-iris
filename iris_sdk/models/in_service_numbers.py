#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.resource import BaseResource

XML_NAME_IN_SERVICE_NUMBERS = "TelephoneNumbers"
XPATH_IN_SERVICE_NUMBERS = "/inserviceNumbers"

class InServiceNumbersData(object):

    @property
    def items(self):
        return self._items

    @property
    def telephone_number(self):
        return self.items

class InServiceNumbers(InServiceNumbersData, BaseResource):

    """In-service numbers for account"""

    _node_name = XML_NAME_IN_SERVICE_NUMBERS
    _xpath = XPATH_IN_SERVICE_NUMBERS

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)
        self._items = []

    def list(self, params=None):
        super().get_raw(params=params, node_name=self._node_name)
        return self.items