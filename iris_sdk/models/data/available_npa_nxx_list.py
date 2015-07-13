#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.npa_nxx import NpaNxx
from iris_sdk.models.maps.available_npa_nxx_list import AvailableNpaNxxListMap

class AvailableNpaNxxList(AvailableNpaNxxListMap, BaseData):

    @property
    def items(self):
        return self.available_npa_nxx.items

    def __init__(self):
        self.available_npa_nxx = BaseResourceList(NpaNxx)