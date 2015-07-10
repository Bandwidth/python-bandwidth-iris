#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.maps.telephone_number_list import TelephoneNumberListMap
from iris_sdk.models.data.telephone_number import TelephoneNumberData

class TelephoneNumberList(TelephoneNumberListMap, BaseData):

    @property
    def items(self):
        return self.telephone_number.items

    def __init__(self):
        self.telephone_number = BaseResourceSimpleList(TelephoneNumberData)

    def add(self, phone_number=None):
        new_phone = self.telephone_number.add()
        if (phone_number is not None):
            new_phone.telephone_number = phone_number
        return new_phone