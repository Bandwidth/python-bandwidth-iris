#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.maps.order_tns import OrderTnsMap

class OrderTnsData(OrderTnsMap, BaseData):

    def __init__(self):
        self.telephone_number = BaseResourceSimpleList()