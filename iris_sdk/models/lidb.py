#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.lidb import LidbData
from iris_sdk.models.lidb_order_response import LidbOrderResponse

XPATH_LIDB = "/{}"

class Lidb(BaseResource, LidbData):

    """ CNAM Update (LIDB) order """

    _xpath = XPATH_LIDB

    @property
    def id(self):
        return self.order_id
    @id.setter
    def id(self, id):
        self.order_id = id

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LidbData.__init__(self)

    def get(self, id=None, params=None):
        order_response = LidbOrderResponse(self._parent)
        order_response.lidb = self
        return order_response.get(id, params=params)

    def save(self):
        str = self._save(True)
        order_response = LidbOrderResponse(self._parent)
        self.clear()
        order_response.lidb = self
        order_response._from_xml(self._element_from_string(str))
        self.order_status = order_response.order_status
        return True