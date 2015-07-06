#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.calling_name import CallingNameMap

class CallingName(CallingNameMap, BaseData):
    pass