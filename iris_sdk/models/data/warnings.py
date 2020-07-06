#!/usr/bin/env python
  
from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.warning import WarningCls 
from iris_sdk.models.maps.warnings import WarningsMap

class Warnings(WarningsMap, BaseData):

    def __init__(self):
        self.warning = BaseResourceList(WarningCls)
