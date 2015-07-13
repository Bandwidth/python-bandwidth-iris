#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.maps.local_rate_center_list import LocalRateCenterListMap

class LocalRateCenterList(LocalRateCenterListMap, BaseData):

    @property
    def items(self):
        return self.local_rate_center_id.items

    def __init__(self):
        self.local_rate_center_id = BaseResourceSimpleList()