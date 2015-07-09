#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.error import Error
from iris_sdk.models.maps.error_list import ErrorListMap

class ErrorList(ErrorListMap, BaseData):

    def __init__(self):
        self.error = BaseResourceList(Error)