#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.tn_rate_center import TnRateCenterMap

class TnRateCenterData(TnRateCenterMap, BaseData):

    @property
    def name(self):
        return self.rate_center
    @name.setter
    def name(self, name):
        self.rate_center = name