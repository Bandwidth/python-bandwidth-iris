#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.portin import PortInData

XML_NAME_PORTIN = "LnpOrderResponse"
XPATH_PORTIN = "/{}"

class PortIn(BaseResource, PortInData):

    """Local number portability order"""

    _node_name = XML_NAME_PORTIN
    _xpath = XPATH_PORTIN

    @property
    def id(self):
        return self.order_id
    @id.setter
    def id(self, id):
        self.order_id = id

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        PortInData.__init__(self)