#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource, BaseResourceList

class VendorsData(object):

    @property
    def items(self):
        return self.vendor_with_count.items

    @property
    def list(self):
        return self.vendor_with_count.items

    @property
    def vendor_with_count(self):
        return self._vendor_with_count

class Vendors(VendorsData):

    def __init__(self):
        self._vendor_with_count = BaseResourceList()
        self._vendor_with_count.items.append(VendorWithCount())

class VendorWithCountData(object):

    @property
    def count(self):
        return self._count
    @count.setter
    def count(self, count):
        self._count = count

    @property
    def id(self):
        return self.vendor_id

    @property
    def name(self):
        return self.vendor_name

    @property
    def vendor_id(self):
        return self._vendor_id
    @vendor_id.setter
    def vendor_id(self, vendor_id):
        self._vendor_id = vendor_id

    @property
    def vendor_name(self):
        return self._vendor_name
    @vendor_name.setter
    def vendor_name(self, vendor_name):
        self._vendor_name = vendor_name

class VendorWithCount(VendorWithCountData):

   def __init__(self):
       self._vendor_id = None
       self._vendor_name = None
       self._count = None