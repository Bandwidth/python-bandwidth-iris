#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.permission import Permission
from iris_sdk.models.maps.permissions_list import PermissionsListMap

class PermissionsList(PermissionsListMap, BaseData):

    @property
    def items(self):
        return self.permission.items

    def __init__(self):
        self.permission = BaseResourceList(Permission)