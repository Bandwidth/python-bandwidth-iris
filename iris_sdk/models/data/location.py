#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.tn_rate_centers_list import TnRateCentersList
from iris_sdk.models.maps.location import LocationMap

class Location(LocationMap, BaseData):

    def __init__(self):
        self.rate_centers = BaseResourceList(TnRateCentersList)