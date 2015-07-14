#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.maps.ttn_list import TnListMap

class TnList(TnListMap, BaseData):

    @property
    def items(self):
        return self.tn.items

    def __init__(self):
        self.tn = BaseResourceSimpleList()

    def add(self, phone_number=None):
        return self.tn.add(phone_number)