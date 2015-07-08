#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.cities_list import CitiesList
from iris_sdk.models.maps.cities import CitiesMap

class CitiesData(CitiesMap, BaseData):

    def __init__(self):
        self.cities = CitiesList()