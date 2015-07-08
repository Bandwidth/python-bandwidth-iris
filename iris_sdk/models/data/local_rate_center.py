#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.local_rate_center import LocalRateCenterMap

class LocalRateCenter(LocalRateCenterMap, BaseData):

    @property
    def id(self):
        return self.rate_center_id
    @id.setter
    def id(self, id):
        self.rate_center_id = id