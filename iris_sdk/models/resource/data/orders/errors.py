#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResourceList

class ErrorData(object):

    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, code):
        self._code = code

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def telephone_number(self):
        return self._telephone_number
    @telephone_number.setter
    def telephone_number(self, telephone_number):
        self._telephone_number = telephone_number

class Error(ErrorData):

    def __init__(self):
        self.clear()

    def clear(self):
        self._code = None
        self._description = None
        self._telephone_number = None

class ErrorListData(object):

    @property
    def error(self):
        return self._error

    @property
    def items(self):
        return self.error.items

class ErrorList(ErrorListData):

    def __init__(self):
        self._error = BaseResourceList()

    def clear(self):
        del self._error.items[:]
        self._error.items.append(Error())