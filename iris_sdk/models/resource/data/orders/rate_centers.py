#!/usr/bin/env python

from __future__ import division, absolute_import, print_function

from iris_sdk.models.base_resource import BaseResourceList

class RateCentersData(object):

    @property
    def items(self):
        return self.rate_center_with_count.items

    @property
    def rate_center_with_count(self):
        return self._rate_center_with_count

class RateCenters(RateCentersData):

    def __init__(self):
        self._rate_center_with_count = BaseResourceList()
        self._rate_center_with_count.items.append(RateCenterWithCount())

class RateCenterWithCountData(object):

    @property
    def count(self):
        return self._count
    @count.setter
    def count(self, count):
        self._count = count

    @property
    def name(self):
        return self.rate_center

    @property
    def rate_center(self):
        return self._rate_center
    @rate_center.setter
    def rate_center(self, rate_center):
        self._rate_center = rate_center

class RateCenterWithCount(RateCenterWithCountData):

   def __init__(self):
       self._rate_center = None
       self._count = None