#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.resource.data.available_numbers.\
    telephone_number_detail_list import TelephoneNumberDetailList
from iris_sdk.models.base_resource import BaseResource

XML_NAME_AVAILABLE_NUMBERS = "SearchResult"
XPATH_AVAILABLE_NUMBERS = "/availableNumbers"
XML_PARAM_TN_DETAIL = "enableTNDetail"
XML_PARAM_TN_DETAIL_TRUE = "true"

class AvailableNumbersData(object):

    @property
    def items(self):
        return self.telephone_number_list

    @property
    def result_count(self):
        return self._result_count
    @result_count.setter
    def result_count(self, result_count):
        self._result_count = result_count

    @property
    def search_count(self):
        return self.result_count

    @property
    def telephone_number_list(self):
        return self._items

    @property
    def telephone_number_detail_list(self):
        return self._telephone_number_detail_list

class AvailableNumbers(AvailableNumbersData, BaseResource):

    """Available numbers for account"""

    _node_name = XML_NAME_AVAILABLE_NUMBERS
    _xpath = XPATH_AVAILABLE_NUMBERS

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)
        self._result_count = None
        self._items = []
        self._telephone_number_detail_list = TelephoneNumberDetailList()

    def clear(self):
        self._result_count = None
        del self._items[:]
        self._telephone_number_detail_list.clear()

    def list(self, params=None):
        self.clear()
        self.get_data(params=params)
        #self._prepare_list(
        #    TelephoneNumberDetailList.telephone_number_detail.items)
        if (params.get(XML_PARAM_TN_DETAIL, "") == XML_PARAM_TN_DETAIL_TRUE):
            return self._telephone_number_detail_list.\
                telephone_number_detail.items
        else:
            return self.telephone_number_list