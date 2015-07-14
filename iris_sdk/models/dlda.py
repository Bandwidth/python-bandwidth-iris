#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.dlda import DldaData
from iris_sdk.models.dlda_order_response import DldaOrderResponse
from iris_sdk.models.history import History

XML_NAME_DLDA = "DldaOrder"
XPATH_DLDA = "/{}"

class Dlda(BaseResource, DldaData):

    """ DLDA order """

    _node_name = XML_NAME_DLDA
    _xpath = XPATH_DLDA

    @property
    def id(self):
        return self.order_id
    @id.setter
    def id(self, id):
        self.order_id = id

    @property
    def history(self):
        return self._history

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        DldaData.__init__(self)
        self._history = History(self, client)

    def get(self, id=None, params=None):
        order_response = DldaOrderResponse(self._parent)
        order_response.dlda_order = self
        return order_response.get(id, params=params)

    def save(self):
        str = self._save(True)
        order_response = DldaOrderResponse(self._parent)
        self.clear()
        order_response.dlda_order = self
        order_response._from_xml(self._element_from_string(str))
        self.order_status = order_response.order_status
        return True