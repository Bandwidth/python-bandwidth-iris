#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.dlda import DldaMap
from iris_sdk.models.data.dlda_tn_groups import DldaTnGroups
from iris_sdk.models.data.error_list import ErrorList


class DldaData(DldaMap, BaseData):
    def __init__(self, parent=None):
        self.dlda_tn_groups = DldaTnGroups(parent=parent)
        self.error_list = ErrorList()()