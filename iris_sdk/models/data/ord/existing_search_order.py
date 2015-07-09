#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.telephone_number_list import TelephoneNumberList
from iris_sdk.models.maps.ord.existing_search_order import \
    ExistingSearchOrderMap

class ExistingSearchOrder(ExistingSearchOrderMap, BaseData):

    def __init__(self):
        self.telephone_number_list = TelephoneNumberList()