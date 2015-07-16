#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.disconnect import DisconnectData
from iris_sdk.models.notes import Notes
from iris_sdk.models.disconnect_order_response import DisconnectOrderResponse

XML_NAME_DISCONNECT = "DisconnectTelephoneNumberOrder"
XPATH_DISCONNECT = "/{}"

class Disconnect(BaseResource, DisconnectData):

    """Disconnect telephone numbers order for account"""

    _node_name = XML_NAME_DISCONNECT
    _xpath = XPATH_DISCONNECT

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
        DisconnectData.__init__(self)
        self._notes = Notes(self, client)

    def get(self, params=None):
        _id = self.id
        order_response = DisconnectOrderResponse(self._parent)
        self.clear()
        order_response.order_request = self
        return order_response.get(_id, params=params)

    def save(self):
        str = self._save(True)
        order_response = DisconnectOrderResponse(self._parent)
        self.clear()
        order_response.order_request = self
        order_response._from_xml(self._element_from_string(str))
        self.order_status = order_response.order_status
        return True