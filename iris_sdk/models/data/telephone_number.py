#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.telephone_number import TelephoneNumberMap

class TelephoneNumber(TelephoneNumberMap, BaseData):

    @property
    def telephone_number(self):
        return self.full_number
    @telephone_number.setter
    def telephone_number(self, number):
        self.full_number = number