#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.links import Links
from iris_sdk.models.maps.orders_view_map import OrdersViewMap
from iris_sdk.models.data.past_order import PastOrder

class OrdersViewData(OrdersViewMap, BaseData):

    def __init__(self, parent=None):
        self.links = Links()
        self.order_id_user_id_date = BaseResourceList(PastOrder, parent)