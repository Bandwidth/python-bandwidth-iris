#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResourceList
from iris_sdk.models.data.telephone_number import TelephoneNumber

class TelephoneNumberDetailListData(object):

    @property
    def telephone_number_detail(self):
        return self._telephone_number_detail

class TelephoneNumberDetailList(TelephoneNumberDetailListData):

    def __init__(self):
        self._telephone_number_detail=BaseResourceList(TelephoneNumber)

    def clear(self):
        self.telephone_number_detail.clear()