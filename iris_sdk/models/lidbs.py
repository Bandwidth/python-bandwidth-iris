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

    def create(self, data=None, save=True):
        lidb = Lidb(self).set_from_dict(data)
        if save and (data is not None):
            lidb.save()
        return lidb

    def get(self, id, params=None):
        return Lidb(self).get(id, params=params)

    def list(self, params):
        return self._get_data(params=params).order_id_user_id_date