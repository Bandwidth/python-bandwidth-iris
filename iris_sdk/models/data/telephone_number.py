#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.features import Features
from iris_sdk.models.maps.telephone_number import TelephoneNumberMap

class TelephoneNumberData(TelephoneNumberMap, BaseData):

    @property
    def id(self):
        return self.full_number
    @id.setter
    def id(self, id):
        self.full_number = id

    @property
    def telephone_number(self):
        return self.full_number
    @telephone_number.setter
    def telephone_number(self, number):
        self.full_number = number

    def __init__(self):
        self.features = Features()