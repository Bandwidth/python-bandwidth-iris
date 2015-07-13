#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.order_response import OrderResponseData

XPATH_ORDER = "/{}"

class OrderResponse(BaseResource, OrderResponseData):

    """Telephone numbers order response"""

    _xpath = XPATH_ORDER

    @property
    def id(self):
        return self.order.order_id
    @id.setter
    def id(self, order_id):
        self.order.order_id = order_id

    @property
    def order(self):
        return self._order
    @order.setter
    def order(self, order):
        self._order = order

    def __init__(self, parent=None, client=None, params=None):
        super().__init__(parent, client)
        OrderResponseData.__init__(self)

    def get(self, id=None):
        return self._get_data((id or self.id))