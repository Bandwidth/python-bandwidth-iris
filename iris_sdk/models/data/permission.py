#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.permission import PermissionMap

class Permission(PermissionMap, BaseData):

    @property
    def name(self):
        return self.permission_name
    @name.setter
    def name(self, name):
        self.permission_name = name