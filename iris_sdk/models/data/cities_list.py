#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.city import City
from iris_sdk.models.maps.cities_list import CitiesListMap

class CitiesList(CitiesListMap, BaseData):

    def __init__(self):
        self.city = BaseResourceList(City)