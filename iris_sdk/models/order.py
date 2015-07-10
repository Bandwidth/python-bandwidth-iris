#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.order import OrderData
from iris_sdk.models.order_response import OrderResponse

XPATH_ORDER = "/{}"

class Order(BaseResource, OrderData):

    """Account telephone numbers order"""

    _xpath = XPATH_ORDER

    @property
    def order_id(self):
        return self.id
    @order_id.setter
    def order_id(self, order_id):
        self.id = order_id

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        OrderData.__init__(self)

    def get(self, id=None):
        order_response = OrderResponse(self._parent)
        order_response.order = self
        return order_response.get((id or self.id))