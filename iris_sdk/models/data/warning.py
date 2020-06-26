#!/usr/bin/env python
  
from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.warning import WarningMap

class WarningCls(WarningMap, BaseData): #Warning is a reserved word in python
    pass
