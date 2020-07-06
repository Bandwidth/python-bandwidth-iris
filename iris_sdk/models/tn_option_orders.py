#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.tn_option_orders import TnOptionOrdersData
from iris_sdk.models.tn_option_order import TnOptionOrder

XML_NAME_TN_OPTION_ORDERS = "TnOptionOrders"
XPATH_TN_OPTION_ORDERS = "/tnoptions"

class TnOptionOrders(BaseResource, TnOptionOrdersData):

    _node_name = XML_NAME_TN_OPTION_ORDERS
    _xpath = XPATH_TN_OPTION_ORDERS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        TnOptionOrdersData.__init__(self, self)

    def create(self, data=None, save=True):
        tn_option_order = TnOptionOrder(self).set_from_dict(data)
        if save and (data is not None):
            tn_option_order.save()
        return tn_option_order

    def get(self, id, params=None):
        return TnOptionOrder(self).get(id, params=params)

    def list(self, params=None):
        return self._get_data(params=params)
