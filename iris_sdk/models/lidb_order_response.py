#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.lidb_order_response import LidbOrderResponseData

XPATH_LIDB_ORDER_RESPONSE = "/{}"

class LidbOrderResponse(BaseResource, LidbOrderResponseData):

    """ CNAM Update (LIDB) order response """

    _xpath = XPATH_LIDB_ORDER_RESPONSE

    @property
    def id(self):
        return self.order.order_id
    @id.setter
    def id(self, order_id):
        self.order.order_id = order_id

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LidbOrderResponseData.__init__(self)

    def get(self, id=None, params=None):
        return self._get_data((id or self.id), params=params)