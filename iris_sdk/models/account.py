#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.account_users import AccountUsers
from iris_sdk.models.available_npa_nxx import AvailableNpaNxx
from iris_sdk.models.available_numbers import AvailableNumbers
from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.account import AccountData
from iris_sdk.models.disc_numbers import DiscNumbers
from iris_sdk.models.reservation import Reservation
from iris_sdk.models.site_hosts import SiteHosts
from iris_sdk.models.in_service_numbers import InServiceNumbers
from iris_sdk.models.orders import Orders
from iris_sdk.models.sites import Sites

XPATH_ACCOUNT = "/accounts/{}"

class Account(BaseResource, AccountData):

    """Iris account"""

    _xpath = XPATH_ACCOUNT

    @property
    def id(self):
        return self.account_id
    @id.setter
    def id(self, id):
        self.account_id = id

    @property
    def available_npa_nxx(self):
        return self._available_npa_nxx

    @property
    def available_numbers(self):
        return self._available_numbers

    @property
    def disconnected_numbers(self):
        return self._disconnected_numbers

    @property
    def hosts(self):
        return self._hosts

    @property
    def in_service_numbers(self):
        return self._in_service_numbers

    @property
    def orders(self):
        return self._orders

    @property
    def sites(self):
        return self._sites

    @property
    def tnreservation(self):
        return self._tnreservation

    @property
    def users(self):
        return self._users

    def __init__(self, parent=None, client=None):
        if (client is not None):
            self.id = client.config.account_id
        super().__init__(parent, client)
        AccountData.__init__(self)
        self._available_npa_nxx = AvailableNpaNxx(self, client)
        self._available_numbers = AvailableNumbers(self, client)
        self._disconnected_numbers = DiscNumbers(self, client)
        self._hosts = SiteHosts(self, client)
        self._in_service_numbers = InServiceNumbers(self, client)
        self._orders = Orders(self, client)
        self._sites = Sites(self, client)
        self._tnreservation = Reservation(self, client)
        self._users = AccountUsers(self, client)

    def get(self, id=None):
        return self._get_data(id)