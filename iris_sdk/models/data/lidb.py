#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.lidb import LidbMap
from iris_sdk.models.lidb_tn_group import LidbTnGroup
from iris_sdk.models.data.error import Error

class LidbData(LidbMap, BaseData):
    def __init__(self, parent=None):
        self.lidb_tn_groups = BaseResourceList(LidbTnGroup, parent=parent)
        self.error_list = BaseResourceList(Error, parent=parent)