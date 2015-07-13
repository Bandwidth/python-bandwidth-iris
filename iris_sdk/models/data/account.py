#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.address import Address
from iris_sdk.models.data.contact import Contact
from iris_sdk.models.data.tier_list import TierList
from iris_sdk.models.maps.account import AccountMap

class AccountData(AccountMap, BaseData):

    def __init__(self):
        self.address = Address()
        self.contact = Contact()
        self.tiers = TierList()