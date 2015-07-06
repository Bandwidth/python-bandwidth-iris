#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResourceSimpleList
from iris_sdk.models.data.links import Links
from iris_sdk.models.data.telephone_number import TelephoneNumber
from iris_sdk.models.maps.in_service_numbers import InServiceNumbersMap

class InServiceNumbersData(InServiceNumbersMap):

    @property
    def result_count(self):
        return self.total_count
    @result_count.setter
    def result_count(self, result_count):
        self._result_count = result_count

    def __init__(self):
        self.links = Links()
        self.telephone_numbers = BaseResourceSimpleList(TelephoneNumber)