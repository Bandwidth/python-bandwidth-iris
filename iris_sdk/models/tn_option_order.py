#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.tn_option_order import TnOptionOrderData

XML_NAME_TN_OPTION_ORDER = "TnOptionOrder"
XPATH_TN_OPTION_ORDER = "/{}"

class TnOptionOrder(BaseResource, TnOptionOrderData):

    _node_name = XML_NAME_TN_OPTION_ORDER
    _xpath = XPATH_TN_OPTION_ORDER

    @property
    def id(self):
        return self.order_id
    @id.setter
    def id(self, id):
        self.order_id = id

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        TnOptionOrderData.__init__(self)

    def get(self, id=None, params=None):
        return self._get_data(id)

    def save(self):
        str = self._save(True)
        self.clear()
        self._from_xml(self._element_from_string(str))
        return True
