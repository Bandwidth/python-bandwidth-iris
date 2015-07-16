#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.dlda_tn_groups import DldaTnGroupsMap
from iris_sdk.models.data.dlda_tn_group import DldaTnGroupData

class DldaTnGroups(DldaTnGroupsMap, BaseData):

    def __init__(self):
        self.dlda_tn_group = BaseResourceList(DldaTnGroupData)
