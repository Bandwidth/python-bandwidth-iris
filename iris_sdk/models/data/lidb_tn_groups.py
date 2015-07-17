#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.lidb_tn_group import LidbTnGroupData
from iris_sdk.models.maps.lidb_tn_groups import LidbTnGroupsMap

class LidbTnGroups(LidbTnGroupsMap, BaseData):

    def __init__(self):
        self.lidb_tn_group = BaseResourceList(LidbTnGroupData)
