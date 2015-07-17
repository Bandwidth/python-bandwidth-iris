#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.lidb import LidbMap
from iris_sdk.models.data.lidb_tn_groups import LidbTnGroups
from iris_sdk.models.data.error_list import ErrorList

class LidbData(LidbMap, BaseData):

    @property
    def count_of_tns(self):
        return self.count_of_t_ns
    @count_of_tns.setter
    def count_of_tns(self, count_of_tns):
        self.count_of_t_ns = count_of_tns

    def __init__(self):
        self.lidb_tn_groups = LidbTnGroups()
        self.error_list = ErrorList()