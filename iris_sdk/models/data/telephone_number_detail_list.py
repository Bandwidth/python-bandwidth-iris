#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.telephone_number import TelephoneNumber
from iris_sdk.models.maps.telephone_number_detail_list import \
    TelephoneNumberDetailListMap

class TelephoneNumberDetailList(TelephoneNumberDetailListMap, BaseData):

    def __init__(self):
        self.telephone_number_detail = BaseResourceList(TelephoneNumber)