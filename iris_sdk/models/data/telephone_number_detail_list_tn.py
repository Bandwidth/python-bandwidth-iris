#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.telephone_number_detail_list_tn import \
    TelephoneNumberDetailListTnMap
from iris_sdk.models.telephone_number import TelephoneNumber

class TelephoneNumberDetailListTn(TelephoneNumberDetailListTnMap, BaseData):

    @property
    def items(self):
        return self.telephone_number.items

    def __init__(self, parent=None):
        self.telephone_number = BaseResourceList(TelephoneNumber, parent)