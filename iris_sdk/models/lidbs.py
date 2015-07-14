#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.lidbs import LidbsData
from iris_sdk.models.lidb import Lidb

XML_NAME_LIDBS = "ListOrderIdUserIdDate"
XPATH_LIDBS = "/lidbs"

class Lidbs(BaseResource, LidbsData):

    """ CNAM Update (LIDB) order """

    _node_name = XML_NAME_LIDBS
    _xpath = XPATH_LIDBS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LidbsData.__init__(self, self)

    def add(self):
        return Lidb(self)

    def get(self, id, params=None):
        return self.add().get(id, params=params)

    def list(self, params):
        return self._get_data(params=params).order_id_user_id_date

    def create(self, initial_data, save=True):
        lidb = self.add()
        lidb.set_from_dict(initial_data)
        if save:
            lidb.save()
        return lidb