#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.available_npa_nxx_list import AvailableNpaNxxList
from iris_sdk.models.maps.available_npa_nxx import AvailableNpaNxxMap

class AvailableNpaNxxData(AvailableNpaNxxMap, BaseData):

    def __init__(self):
        self.available_npa_nxx_list = AvailableNpaNxxList()