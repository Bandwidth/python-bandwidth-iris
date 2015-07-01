#!/usr/bin/env python

class TierData(object):

    @property
    def tier(self):
        return self._tier
    @tier.setter
    def tier(self, tier):
        self._tier = tier

class Tier(TierData):

    def __init__(self):
        self.clear()

    def clear(self):
        self.tier = None