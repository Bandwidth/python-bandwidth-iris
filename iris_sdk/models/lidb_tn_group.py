#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.lidb_tn_group import LidbTnGroupData

XPATH_LIDB_TN_GROUP = "/{}"

class LidbTnGroup(BaseResource, LidbTnGroupData):

    _xpath = XPATH_LIDB_TN_GROUP

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LidbTnGroupData.__init__(self)