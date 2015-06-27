#!/usr/bin/env python

#from abc import ABC

class TiersData(object):

    @property
    def tiers(self):
        return self._items

    @property
    def tier(self):
        return self.tiers

class Tiers(TiersData):

    def __init__(self):
        self._items = []