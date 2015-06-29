#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.resource.available_numbers import AvailableNumbers
from iris_sdk.models.resource.data.accounts.contact import Contact
from iris_sdk.models.resource.data.common.address import Address
from iris_sdk.models.resource.in_service_numbers import InserviceNumbers
from iris_sdk.models.resource.orders import Orders

XPATH_ACCOUNT = "/accounts/{}"

class AccountData(object):

    @property
    def account_id(self):
        return self._account_id
    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def account_type(self):
        return self._account_type
    @account_type.setter
    def account_type(self, account_type):
        self._account_type = account_type

    @property
    def address(self):
        return self._address

    @property
    def alt_spid(self):
        return self._alt_spid
    @alt_spid.setter
    def alt_spid(self, alt_spid):
        self._alt_spid = alt_spid

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
    def in_service_numbers(self):
        return self._in_service_numbers

    @property
    def is_new_sms_account(self):
        return self._is_new_sms_account
    @is_new_sms_account.setter
    def is_new_sms_account(self, is_new_sms_account):
        self._is_new_sms_account = is_new_sms_account

    @property
    def lnp_enabled(self):
        return self._lnp_enabled
    @lnp_enabled.setter
    def lnp_enabled(self, lnp_enabled):
        self._lnp_enabled = lnp_enabled

    @property
    def nena_id(self):
        return self._nena_id
    @nena_id.setter
    def nena_id(self, nena_id):
        self._nena_id = nena_id

    @property
    def orders(self):
        return self._orders

    @property
    def port_carrier_type(self):
        return self._port_carrier_type
    @port_carrier_type.setter
    def port_carrier_type(self, port_carrier_type):
        self._port_carrier_type = port_carrier_type

    @property
    def reservation_allowed(self):
        return self._reservation_allowed
    @reservation_allowed.setter
    def reservation_allowed(self, reservation_allowed):
        self._reservation_allowed = reservation_allowed

    @property
    def spid(self):
        return self._spid
    @spid.setter
    def spid(self, spid):
        self._spid = spid

    @property
    def tiers(self):
        return self._tiers

    @property
    def tiers_list(self):
        return self.tiers.items

class Account(AccountData, BaseResource):

    """Iris account"""

    _xpath = XPATH_ACCOUNT

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)
        self._account_id = None
        self._account_type = None
        self._alt_spid = None
        self._company_name = None
        self._customer_name = None
        self._description = None
        self._is_new_sms_account = None
        self._lnp_enabled = None
        self._nena_id = None
        self._port_carrier_type = None
        self._reservation_allowed = None
        self._spid = None
        self._address = Address()
        self._contact = Contact()
        self._tiers = []
        self._available_numbers = AvailableNumbers(client, self._xpath)
        self._in_service_numbers = InserviceNumbers(client, self._xpath)
        self._orders = Orders(client, self._xpath)

    def clear(self):
        del self._tiers[:]
        self._account_id = None
        self._account_type = None
        self._alt_spid = None
        self._company_name = None
        self._customer_name = None
        self._description = None
        self._is_new_sms_account = None
        self._lnp_enabled = None
        self._nena_id = None
        self._port_carrier_type = None
        self._reservation_allowed = None
        self._spid = None
        self._address.clear()
        self._contact.clear()

    def get(self):
        self.clear()
        return self.get_data()