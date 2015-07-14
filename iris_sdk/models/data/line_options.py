#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.line_options import LineOptionsMap
from iris_sdk.models.data.error_list import ErrorList
from iris_sdk.models.data.telephone_number_list import TelephoneNumberList

class LineOptionsData(LineOptionsMap, BaseData):

    def __init__(self, parent=None):
        self.complete_numbers = TelephoneNumberList()
        self.errors = ErrorList()