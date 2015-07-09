#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.data.telephone_number import TelephoneNumberData
from iris_sdk.models.maps.disc_numbers import DiscNumbersMap

class DiscNumbersData(DiscNumbersMap, BaseData):

    def __init__(self):
        self.telephone_number_list=BaseResourceSimpleList(TelephoneNumberData)