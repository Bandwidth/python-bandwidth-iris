#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.lidb_order_response import LidbOrderResponseData

class LidbOrderResponse(BaseResource, LidbOrderResponseData):

    """ CNAM Update (LIDB) order response """

    @property
    def id(self):
        return self.lidb_order.order_id
    @id.setter
    def id(self, order_id):
        self.lidb_order.order_id = order_id

    @property
    def lidb_order(self):
        return self._lidb_order
    @lidb_order.setter
    def lidb_order(self, lidb_order):
        self._lidb_order = lidb_order

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LidbOrderResponseData.__init__(self)