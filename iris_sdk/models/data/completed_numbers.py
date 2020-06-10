#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.data.full_numbers import FullNumbers
from iris_sdk.models.maps.completed_numbers import CompletedNumbersMap

class CompletedNumbers(CompletedNumbersMap, BaseData):

    @property
    def items(self):
        return self.telephone_number.items

    def __init__(self):
        self.telephone_number = FullNumbers()

    def add(self, phone_number=None):
        return self.telephone_number.add(phone_number)
