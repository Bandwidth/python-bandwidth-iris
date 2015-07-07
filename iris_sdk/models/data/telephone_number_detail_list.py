#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.telephone_number_detail_list import \
    TelephoneNumberDetailListMap
from iris_sdk.models.telephone_number import TelephoneNumber

class TelephoneNumberDetailList(TelephoneNumberDetailListMap, BaseData):

    def __init__(self, parent=None):
        self.telephone_number_detail = \
            BaseResourceList(TelephoneNumber, parent)