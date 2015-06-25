#!/usr/bin/env python

#from abc import ABC

class TiersData():

    @property
    def items(self):
        return self._items

    @property
    def tier(self):
        return self.items

class Tiers(TiersData):

    def __init__(self):
        self._items = []