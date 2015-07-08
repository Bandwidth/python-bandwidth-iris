#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.role import Role
from iris_sdk.models.maps.roles_list import RolesListMap

class RolesList(RolesListMap, BaseData):

    @property
    def items(self):
        return self.role.items

    def __init__(self):
        self.role = BaseResourceList(Role)