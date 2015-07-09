#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.maps.telephone_number_list import TelephoneNumberListMap
from iris_sdk.models.data.telephone_number import TelephoneNumberData

class TelephoneNumberList(TelephoneNumberListMap, BaseData):

    def __init__(self):
        self.telephone_number = BaseResourceSimpleList(TelephoneNumberData)