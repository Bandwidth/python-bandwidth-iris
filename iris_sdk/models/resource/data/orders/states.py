#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource, BaseResourceList

class StatesData(object):

    @property
    def items(self):
        return self.state_with_count.items

    @property
    def list(self):
        return self.state_with_count.items

    @property
    def state_with_count(self):
        return self._state_with_count

class States(StatesData):

    def __init__(self):
        self._state_with_count = BaseResourceList()
        self._state_with_count.items.append(StateWithCount())

class StateWithCountData(object):

    @property
    def count(self):
        return self._count
    @count.setter
    def count(self, count):
        self._count = count

    @property
    def name(self):
        return self.state

    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, state):
        self._state = state

class StateWithCount(StateWithCountData):

   def __init__(self):
       self._state = None
       self._count = None