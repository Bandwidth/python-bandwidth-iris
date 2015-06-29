#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource, BaseResourceList

class CitiesData(object):

    @property
    def items(self):
        return self.city_with_count.items

    @property
    def list(self):
        return self.city_with_count.items

    @property
    def city_with_count(self):
        return self._city_with_count

class Cities(CitiesData):

    def __init__(self):
        self._city_with_count = BaseResourceList()
        self._city_with_count.items.append(CityWithCount())

class CityWithCountData(object):

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, city):
        self._city = city

    @property
    def count(self):
        return self._count
    @count.setter
    def count(self, count):
        self._count = count

    @property
    def name(self):
        return self.city

class CityWithCount(CityWithCountData):

   def __init__(self):
       self._city = None
       self._count = None