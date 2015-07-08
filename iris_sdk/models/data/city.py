#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.city import CityMap

class City(CityMap, BaseData):
    pass