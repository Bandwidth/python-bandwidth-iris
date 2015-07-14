#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.dlda_order_response import DldaOrderResponseData

XPATH_DLDA_ORDER_RESPONSE = "/{}"

class DldaOrderResponse(BaseResource, DldaOrderResponseData):

    """ DLDA order response """

    _xpath = XPATH_DLDA_ORDER_RESPONSE

    @property
    def id(self):
        return self.dlda_order.order_id
    @id.setter
    def id(self, order_id):
        self.dlda_order.order_id = order_id

    @property
    def dlda_order(self):
        return self._dlda_order
    @dlda_order.setter
    def dlda_order(self, dlda_order):
        self._dlda_order = dlda_order

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        DldaOrderResponseData.__init__(self)

    def get(self, id=None, params=None):
        return self._get_data((id or self.id), params=params)