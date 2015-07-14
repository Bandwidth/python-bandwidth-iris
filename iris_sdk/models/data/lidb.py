#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.lidb import LidbMap
from iris_sdk.models.data.lidb_tn_groups import LidbTnGroups
from iris_sdk.models.data.error_list import ErrorList

class LidbData(LidbMap, BaseData):
    def __init__(self, parent=None):
        self.lidb_tn_groups = LidbTnGroups(parent=parent)
        self.error_list = ErrorList()