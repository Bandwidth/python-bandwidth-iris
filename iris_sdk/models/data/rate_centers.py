#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.rate_centers_list import RateCentersList
from iris_sdk.models.maps.rate_centers import RateCentersMap

class RateCentersData(RateCentersMap, BaseData):

    def __init__(self):
        self.rate_centers = RateCentersList()