#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.line_option_order import LineOptionOrderData
from iris_sdk.models.line_option_order_response import LineOptionOrderResponse

XML_NAME_LINE_OPTION_ORDERS = "LineOptionOrder"
XPATH_LINE_OPTION_ORDERS = "/lineOptionOrders"

class LineOptionOrder(BaseResource, LineOptionOrderData):

    """
    Establish Calling Name Display settings for a collection of TNs at a time
    """

    _node_name = XML_NAME_LINE_OPTION_ORDERS
    _save_post = True
    _xpath = XPATH_LINE_OPTION_ORDERS
    _xpath_save = _xpath

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LineOptionOrderData.__init__(self)

    def save(self):
        response = LineOptionOrderResponse(self._parent)
        return self._post_data(response)