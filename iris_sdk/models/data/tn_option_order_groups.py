#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.tn_option_order_groups import TnOptionOrderGroupsMap
from iris_sdk.models.data.tn_option_order_group import TnOptionOrderGroupData

class TnOptionOrderGroupsData(TnOptionOrderGroupsMap, BaseData):

    def __init__(self, parent=None):
        self.tn_option_group = BaseResourceList(TnOptionOrderGroupData, parent)
