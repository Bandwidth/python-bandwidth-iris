#!/usr/bin/env python

from iris_sdk.models.data.telephone_number_detail_list import \
    TelephoneNumberDetailList
from iris_sdk.models.maps.telephone_numbers import TelephoneNumbersMap

class TelephoneNumbers(TelephoneNumbersMap, TelephoneNumberDetailList):

    @property
    def telephone_number(self):
        return self.telephone_number_detail

    def __init__(self, parent=None):
        TelephoneNumberDetailList.__init__(self, parent)