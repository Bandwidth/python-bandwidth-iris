#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.links import Links
from iris_sdk.models.data.telephone_number_list import TelephoneNumberList
from iris_sdk.models.maps.in_service_numbers import InServiceNumbersMap

class InServiceNumbersData(InServiceNumbersMap, BaseData):

    def __init__(self):
        self.links = Links()
        self.telephone_numbers = TelephoneNumberList()