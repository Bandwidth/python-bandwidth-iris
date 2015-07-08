#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.links import Links
from iris_sdk.models.rate_center import RateCenter
from iris_sdk.models.maps.covered_rate_centers import CoveredRateCentersMap

class CoveredRateCentersData(CoveredRateCentersMap, BaseData):

    @property
    def result_count(self):
        return self.total_count
    @result_count.setter
    def result_count(self, result_count):
        self.total_count = result_count

    def __init__(self, parent=None):
        self.links = Links()
        self.covered_rate_center = BaseResourceList(RateCenter, parent)