#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.city import CityMap

class City(CityMap, BaseData):

    @property
    def city(self):
        return name
    @city.setter
    def city(self, city):
        self.name = city