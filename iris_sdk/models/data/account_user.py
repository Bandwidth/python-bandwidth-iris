#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.roles_list import RolesList
from iris_sdk.models.maps.account_user import AccountUserMap

class AccountUser(AccountUserMap, BaseData):

    def __init__(self):
        self.roles = RolesList()