#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.disconnects import DisconnectsData
from iris_sdk.models.disconnect import Disconnect

XML_NAME_DISCONNECTS = "ListOrderIdUserIdDate"
XPATH_DISCONNECTS = "/disconnects"

class Disconnects(BaseResource, DisconnectsData):

    """Disconnect telephone numbers orders for account"""

    _node_name = XML_NAME_DISCONNECTS
    _xpath = XPATH_DISCONNECTS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        DisconnectsData.__init__(self, self)

    def create(self, data=None, save=True):
        disconnect = Disconnect(self).set_from_dict(data)
        if save and (data is not None):
            disconnect.save()
        return disconnect

    def get(self, id, params=None):
        return self.add().get(id, params=params)

    def list(self, params):
        return self._get_data(params=params).order_id_user_id_date