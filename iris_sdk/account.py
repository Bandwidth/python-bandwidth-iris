#!/usr/bin/env python

#from abc import ABC

from iris_sdk.models.address import Address
from iris_sdk.models.available_numbers import AvailableNumbers
from iris_sdk.models.contact import Contact
from iris_sdk.models.resource import BaseResource
from iris_sdk.models.tiers import Tiers

XPATH_ACCOUNT = "/accounts/{}"

class AccountData():

    @property
    def address(self):
        return self._address

    @property
    def available_numbers(self):
        return self._available_numbers

    @property
    def company_name(self):
        return self._company_name
    @company_name.setter
    def company_name(self, company_name):
        self._company_name = company_name

    @property
    def contact(self):
        return self._contact

    @property
    def customer_name(self):
        return self._customer_name
    @customer_name.setter
    def customer_name(self, customer_name):
        self._customer_name = customer_name

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def account_id(self):
        return self._account_id
    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def tiers(self):
        return self._tiers


class Account(AccountData, BaseResource):

    """Iris account"""

    _xpath = XPATH_ACCOUNT

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)
        self._address = Address()
        self._contact = Contact()
        self._tiers = Tiers()
        self._available_numbers = AvailableNumbers(client, self._xpath)

    def available_numbers_list(self, params=None):
        self._available_numbers.list(params)
        return self._available_numbers.items

    def get(self):
        return super().get_raw()