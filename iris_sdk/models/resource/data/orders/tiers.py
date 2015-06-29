#!/usr/bin/env python

from __future__ import division, absolute_import, print_function

from iris_sdk.models.base_resource import BaseResourceList

class TiersData(object):

    @property
    def items(self):
        return self.tier_with_count.items

    @property
    def tier_with_count(self):
        return self._tier_with_count

class Tiers(TiersData):

    def __init__(self):
        self._tier_with_count = BaseResourceList()
        self._tier_with_count.items.append(TierWithCount())

class TierWithCountData(object):

    @property
    def count(self):
        return self._count
    @count.setter
    def count(self, count):
        self._count = count

    @property
    def name(self):
        return self.tier

    @property
    def tier(self):
        return self._tier
    @tier.setter
    def tier(self, tier):
        self._tier = tier

class TierWithCount(TierWithCountData):

   def __init__(self):
       self._tier = None
       self._count = None