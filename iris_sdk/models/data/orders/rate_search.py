#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

class RateCenterSearchAndOrderTypeData(object):

    @property
    def rate_center(self):
        return self._rate_center
    @rate_center.setter
    def rate_center(self, rate_center):
        self._rate_center = rate_center

    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, state):
        self._state = state

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

class RateCenterSearchAndOrderType(RateCenterSearchAndOrderTypeData):

    def __init__(self):
        self.clear()

    def clear(self):
        self._rate_center = None
        self._state = None
        self._quantity = None