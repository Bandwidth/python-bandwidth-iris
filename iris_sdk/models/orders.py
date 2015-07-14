#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.orders import OrdersData
from iris_sdk.models.order import Order

XML_NAME_ORDERS = "ListOrderIdUserIdDate"
XPATH_ORDERS = "/orders"

class Orders(BaseResource, OrdersData):

    """Telephone number orders for account"""

    _node_name = XML_NAME_ORDERS
    _xpath = XPATH_ORDERS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        OrdersData.__init__(self, self)

    def add(self, data=None, save=True):
        order = Order(self).set_from_dict(data)
        if save:
            order.save()
        return order

    def get(self, id, params=None):
        return self.add(save=False).get(id, params=params)

    def list(self, params):
        return self._get_data(params=params).order_id_user_id_date