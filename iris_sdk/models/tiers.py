#!/usr/bin/env python

class Tiers():

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @property
    def tier(self):
        return self.items