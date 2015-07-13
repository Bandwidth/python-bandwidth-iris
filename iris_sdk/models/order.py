#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.order import OrderData
from iris_sdk.models.notes import Notes
from iris_sdk.models.order_response import OrderResponse

XPATH_ORDER = "/{}"

class Order(BaseResource, OrderData):

    """Account telephone numbers order"""

    _xpath = XPATH_ORDER

    @property
    def id(self):
        return self.order_id
    @id.setter
    def id(self, id):
        self.order_id = id

    @property
    def notes(self):
        return self._notes

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        OrderData.__init__(self)
        self._notes = Notes(self, client)

    def get(self, id=None):
        order_response = OrderResponse(self._parent)
        order_response.order = self
        return order_response.get(id)

    def save(self):
        str = self._save(True)
        order_response = OrderResponse(self._parent)
        order_response.order = self
        order_response._from_xml(self._element_from_string(str))
        self.order_status = order_response.order_status
        return True