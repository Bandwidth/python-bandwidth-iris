#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.order_response import OrderResponseData

XML_NAME_DISCONNECT_ORDER_RESPONSE = "DisconnectTelephoneNumberOrderResponse"
XPATH_DISCONNECT_ORDER_RESPONSE = "/{}"

class DisconnectOrderResponse(BaseResource, OrderResponseData):

    """Telephone numbers disconnect order response"""

    _node_name = XML_NAME_DISCONNECT_ORDER_RESPONSE
    _xpath = XPATH_DISCONNECT_ORDER_RESPONSE

    @property
    def id(self):
        return self.order_request.order_id
    @id.setter
    def id(self, order_id):
        self.order_request.order_id = order_id

    @property
    def order_request(self):
        return self._order
    @order_request.setter
    def order_request(self, order_request):
        self._order = order_request

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        OrderResponseData.__init__(self)

    def get(self, id=None, params=None):
        return self._get_data((id or self.id), params=params)