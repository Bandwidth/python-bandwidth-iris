#!/usr/bin/env python

from iris_sdk.include.xml_consts import XML_PARAM_TN_DETAIL, XML_TRUE
from iris_sdk.models.base_resource import BaseResource, BaseResourceSimpleList
from iris_sdk.models.data.telephone_number import TelephoneNumber
from iris_sdk.models.data.telephone_number_detail_list import \
    TelephoneNumberDetailList
from iris_sdk.models.maps.available_numbers import AvailableNumbersMap

XML_NAME_AVAILABLE_NUMBERS = "SearchResult"
XPATH_AVAILABLE_NUMBERS = "/availableNumbers"

class AvailableNumbers(AvailableNumbersMap, BaseResource):

    """Available numbers for account"""

    _node_name = XML_NAME_AVAILABLE_NUMBERS
    _xpath = XPATH_AVAILABLE_NUMBERS

    telephone_number_detail_list = TelephoneNumberDetailList()
    telephone_number_list = BaseResourceSimpleList(TelephoneNumber)

    def list(self, params=None):
        self.get_data(params=params)
        if ((params.get(XML_PARAM_TN_DETAIL, "").lower()) == XML_TRUE):
            return self.telephone_number_detail_list.telephone_number_detail
        else:
            return self.telephone_number_list