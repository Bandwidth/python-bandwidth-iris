#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.permissions_list import PermissionsList
from iris_sdk.models.maps.role import RoleMap

class Role(RoleMap, BaseData):

    @property
    def name(self):
        return self.role_name
    @name.setter
    def name(self, name):
        self.role_name = name

    def __init__(self):
        self.permissions = PermissionsList()