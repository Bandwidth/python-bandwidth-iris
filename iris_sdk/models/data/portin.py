#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.error_list import ErrorList
from iris_sdk.models.maps.portin import PortInMap

class PortInData(PortInMap, BaseData):

    @property
    def count_of_tns(self):
        return self.count_of_t_ns
    @count_of_tns.setter
    def count_of_tns(self, count_of_tns):
        self.count_of_t_ns = count_of_tns

    def __init__(self):
        self.errors = ErrorList()
        self.list_of_phone_numbers = 