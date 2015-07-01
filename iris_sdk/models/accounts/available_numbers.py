#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource, BaseResourceSimpleList
from iris_sdk.models.data.telephone_number import TelephoneNumber
from iris_sdk.models.data.telephone_number_detail_list import \
    TelephoneNumberDetailList

XML_NAME_AVAILABLE_NUMBERS = "SearchResult"
XPATH_AVAILABLE_NUMBERS = "/availableNumbers"
XML_PARAM_TN_DETAIL = "enableTNDetail"
XML_TRUE = "true"

class AvailableNumbersData(object):

    @property
    def result_count(self):
        return self._result_count
    @result_count.setter
    def result_count(self, result_count):
        self._result_count = result_count

    @property
    def telephone_number_detail_list(self):
        return self._telephone_number_detail_list

    @property
    def telephone_number_list(self):
        return self._telephone_number_list

class AvailableNumbers(AvailableNumbersData, BaseResource):

    """Available numbers for account"""

    _node_name = XML_NAME_AVAILABLE_NUMBERS
    _xpath = XPATH_AVAILABLE_NUMBERS

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)
        self._result_count = None
        self._telephone_number_detail_list = TelephoneNumberDetailList()
        self._telephone_number_list = BaseResourceSimpleList(TelephoneNumber)

    def clear(self):
        self.result_count = None
        self.telephone_number_detail_list.clear()
        self.telephone_number_list.clear()

    def list(self, params=None):
        self.clear()
        self.get_data(params=params)
        if ((params.get(XML_PARAM_TN_DETAIL, "").lower()) == XML_TRUE):
            return self.telephone_number_detail_list.telephone_number_detail
        else:
            return self.telephone_number_list