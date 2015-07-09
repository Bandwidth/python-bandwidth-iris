#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.error import ErrorMap

class Error(ErrorMap, BaseData):
    pass