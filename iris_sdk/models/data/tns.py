#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.links import Links
from iris_sdk.models.data.listing_name import ListingName
from iris_sdk.models.maps.tns import TnsMap

class TnsData(TnsMap, BaseData):

    @property
    def result_count(self):
        return self.telephone_number_count
    @result_count.setter
    def result_count(self, result_count):
        self.telephone_number_count = result_count

    def __init__(self):
        self.links = Links()