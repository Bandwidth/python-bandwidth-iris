#!/usr/bin/env python
  
from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.tn_option_order import TnOptionOrderMap
from iris_sdk.models.data.error_list import ErrorList
from iris_sdk.models.data.warnings import Warnings
from iris_sdk.models.data.tn_option_order_groups import TnOptionOrderGroupsData

class TnOptionOrderData(TnOptionOrderMap, BaseData):

    def __init__(self):
        self.error_list = ErrorList()
        self.warnings = Warnings()
        self.tn_option_groups = TnOptionOrderGroupsData()
