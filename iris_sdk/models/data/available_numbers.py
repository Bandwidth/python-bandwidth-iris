#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResource, BaseResourceSimpleList
from iris_sdk.models.data.telephone_number import TelephoneNumber
from iris_sdk.models.data.telephone_number_detail_list import \
    TelephoneNumberDetailList
from iris_sdk.models.maps.available_numbers import AvailableNumbersMap

class AvailableNumbersData(AvailableNumbersMap):

    def __init__(self):
        self.telephone_number_detail_list = TelephoneNumberDetailList()
        self.telephone_number_list = BaseResourceSimpleList(TelephoneNumber)