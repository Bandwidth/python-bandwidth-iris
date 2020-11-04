#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.maps.import_tn_checker_list import TnListMap

class TelephoneNumbers(TnListMap, BaseData):

    @property
    def items(self):
        return self.telephone_number.items

    def __init__(self):
        self.telephone_number = BaseResourceSimpleList()

    def add(self, phone_number=None):
        return self.telephone_number.add(phone_number)
