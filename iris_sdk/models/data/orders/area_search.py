#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

class AreaCodeSearchAndOrderTypeData(object):

    @property
    def area_code(self):
        return self._area_code
    @area_code.setter
    def area_code(self, area_code):
        self._area_code = area_code

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

class AreaCodeSearchAndOrderType(AreaCodeSearchAndOrderTypeData):

    def __init__(self):
        self.clear()

    def clear(self):
        self._area_code = None
        self._quantity = None