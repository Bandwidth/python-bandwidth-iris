#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.lidb_tn_groups import LidbTnGroupsMap
from iris_sdk.models.lidb_tn_group import LidbTnGroup

class LidbTnGroups(LidbTnGroupsMap, BaseData):

    def __init__(self, parent=None):
        self.lidb_tn_group = BaseResourceList(LidbTnGroup, parent=parent)
