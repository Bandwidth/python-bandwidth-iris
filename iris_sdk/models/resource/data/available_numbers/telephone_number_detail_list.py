#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.resource.data.available_numbers.telephone_number_detail\
import TelephoneNumberDetail
from iris_sdk.models.base_resource import BaseResourceList

class TelephoneNumberDetailListData(object):

    @property
    def telephone_number_detail(self):
        return self._telephone_number_detail

class TelephoneNumberDetailList(TelephoneNumberDetailListData):

    def __init__(self):
        self._telephone_number_detail = BaseResourceList()

    def clear(self):
        del self._telephone_number_detail.items[:]
        self._telephone_number_detail.items.append(TelephoneNumberDetail())
        print(self._telephone_number_detail.items[0].state or "")