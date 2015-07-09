#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.ord.city_search_order import CitySearchOrderMap

class CitySearchOrder(CitySearchOrderMap, BaseData):
    pass