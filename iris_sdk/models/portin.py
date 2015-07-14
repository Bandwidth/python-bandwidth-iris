#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.portin import PortInData
from iris_sdk.models.loas import Loas

XML_NAME_PORTIN = "LnpOrderResponse"
XML_NAME_PORTIN_SAVE = "LnpOrder"
XPATH_PORTIN = "/{}"

class PortIn(BaseResource, PortInData):

    """Local number portability order"""

    _node_name = XML_NAME_PORTIN
    _node_name_save = XML_NAME_PORTIN_SAVE
    _xpath = XPATH_PORTIN

    @property
    def id(self):
        return self.order_id
    @id.setter
    def id(self, id):
        self.order_id = id

    @property
    def loas(self):
        return self._loas

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        PortInData.__init__(self)
        self._loas = Loas(self, client)

    def save(self):
        return self._post_data()