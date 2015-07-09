#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.orders import OrdersData

XML_NAME_ORDERS = "ListOrderIdUserIdDate"
XPATH_ORDERS = "/orders"

class Orders(BaseResource, OrdersData):

    """Telephone number orders for account"""

    _node_name = XML_NAME_ORDERS
    _xpath = XPATH_ORDERS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        OrdersData.__init__(self, self)

    #def get(self, id):
    #    return RateCenter(self).get(id)

    def list(self, params):
        self._get_data(params=params)
        return self._get_data(params=params).order_id_user_id_date