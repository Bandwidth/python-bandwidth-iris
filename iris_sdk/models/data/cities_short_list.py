#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.maps.cities_short_list import CitiesShortListMap

class CitiesShortList(CitiesShortListMap, BaseData):

    @property
    def items(self):
        return self.city.items

    def __init__(self):
        self.city = BaseResourceSimpleList()