#!/usr/bin/env python
  
from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.tn_option_orders import TnOptionOrdersMap
from iris_sdk.models.tn_option_order import TnOptionOrder

class TnOptionOrdersData(TnOptionOrdersMap, BaseData):

    def __init__(self, parent=None):
        self.tn_option_order_summary = BaseResourceList(TnOptionOrder, parent)
        self.tn_option_order = BaseResourceList(TnOptionOrder, parent)
