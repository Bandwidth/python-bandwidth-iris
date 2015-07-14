#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.dlda_tn_groups import DldaTnGroupsMap
from iris_sdk.models.dlda_tn_group import DldaTnGroup

class DldaTnGroups(DldaTnGroupsMap, BaseData):

    def __init__(self, parent=None):
        self.dlda_tn_group = BaseResourceList(DldaTnGroup, parent=parent)
