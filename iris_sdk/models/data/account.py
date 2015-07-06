#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResourceSimpleList
from iris_sdk.models.data.address import Address
from iris_sdk.models.data.contact import Contact
from iris_sdk.models.data.tier import Tier
from iris_sdk.models.maps.account import AccountMap

class AccountData(AccountMap):

    def __init__(self):
        self.address = Address()
        self.contact = Contact()
        self.tiers = BaseResourceSimpleList(Tier)