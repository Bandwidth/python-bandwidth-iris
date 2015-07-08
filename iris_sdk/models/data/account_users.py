#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.account_user import AccountUser
from iris_sdk.models.maps.account_users import AccountUsersMap

class AccountUsersData(AccountUsersMap, BaseData):

    def __init__(self):
        self.user = BaseResourceList(AccountUser)