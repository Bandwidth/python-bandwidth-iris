#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.rate_center import RateCenterData
from iris_sdk.models.maps.rate_centers_list import RateCentersListMap

class RateCentersList(RateCentersListMap, BaseData):

    def __init__(self):
        self.rate_center = BaseResourceList(RateCenterData)