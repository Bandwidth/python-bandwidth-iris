#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

class CompletedNumbersData(object):

    @property
    def telephone_number(self):
        return self._telephone_number

class CompletedNumbers(CompletedNumbersData):

    def __init__(self):
        self._telephone_number = []

    def clear(self):
        del self._telephone_number[:]