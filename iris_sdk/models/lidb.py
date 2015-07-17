#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.lidb import LidbData

XML_NAME_LIDB = "LidbOrder"
XPATH_LIDB = "/{}"

class Lidb(BaseResource, LidbData):

    """ CNAM Update (LIDB) order """

    _node_name = XML_NAME_LIDB
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
        return self._get_data(id, params=params)

    def save(self):
        return self._post_data()