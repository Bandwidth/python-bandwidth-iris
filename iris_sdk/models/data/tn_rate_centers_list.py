#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.data.tn_rate_center import TnRateCenterData
from iris_sdk.models.maps.tn_rate_centers_list import TnRateCentersListMap

class TnRateCentersList(TnRateCentersListMap, BaseData):

    @property
    def rcs(self):
        return self.r_cs

    def __init__(self):
        self.r_cs = BaseResourceSimpleList(TnRateCenterData)