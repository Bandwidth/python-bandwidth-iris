#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.links import Links
from iris_sdk.models.maps.orders import OrdersMap
from iris_sdk.models.order_response import OrderResponse

class OrdersData(OrdersMap, BaseData):

    def __init__(self, parent=None):
        self.links = Links()
        self.order = 
        self.order_id_user_id_date = BaseResourceList(OrderResponse, parent)