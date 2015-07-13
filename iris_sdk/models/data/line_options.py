#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.line_options import LineOptionsMap
from iris_sdk.models.data.error import Error
from iris_sdk.models.telephone_number import TelephoneNumber

class LineOptionsData(LineOptionsMap, BaseData):

    def __init__(self, parent=None):
        self.complete_numbers = BaseResourceList(TelephoneNumber, parent)
        self.errors = BaseResourceList(Error, parent)