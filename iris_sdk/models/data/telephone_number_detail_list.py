#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.telephone_number_detail_list import \
    TelephoneNumberDetailListMap
from iris_sdk.models.data.telephone_number import TelephoneNumberData

class TelephoneNumberDetailList(TelephoneNumberDetailListMap, BaseData):

    @property
    def items(self):
        return self.telephone_number_detail.items

    def __init__(self):
        self.telephone_number_detail = BaseResourceList(TelephoneNumberData)