#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.account_users import AccountUsers
from iris_sdk.models.available_npa_nxx import AvailableNpaNxx
from iris_sdk.models.available_numbers import AvailableNumbers
from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.account import AccountData
from iris_sdk.models.disc_numbers import DiscNumbers
from iris_sdk.models.disconnects import Disconnects
from iris_sdk.models.in_service_numbers import InServiceNumbers
from iris_sdk.models.line_option_orders import LineOptionOrder
from iris_sdk.models.import_tn_checker import ImportTnChecker
from iris_sdk.models.lnpchecker import LnpChecker
from iris_sdk.models.orders import Orders
from iris_sdk.models.lidbs import Lidbs
from iris_sdk.models.dldas import Dldas
from iris_sdk.models.subscriptions import Subscriptions
from iris_sdk.models.portins import PortIns
from iris_sdk.models.portouts import PortOuts
from iris_sdk.models.reservation import Reservation
from iris_sdk.models.site_hosts import SiteHosts
from iris_sdk.models.sites import Sites
from iris_sdk.models.tn_option_orders import TnOptionOrders

XPATH_ACCOUNT = "/accounts/{}"

class Account(BaseResource, AccountData):

    """Iris account"""

    _xpath = XPATH_ACCOUNT

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
    def disconnects(self):
        return self._disconnects

    @property
    def dldas(self):
        return self._dldas

    @property
    def hosts(self):
        return self._hosts

    @property
    def id(self):
        return self.account_id
    @id.setter
    def id(self, id):
        self.account_id = id

    @property
    def import_tn_checker(self):
        return self._import_tn_checker

    @property
    def in_service_numbers(self):
        return self._in_service_numbers

    @property
    def lidbs(self):
        return self._lidbs

    @property
    def line_option_orders(self):
        return self._line_option_orders

    @property
    def lnpchecker(self):
        return self._lnpchecker

    @property
    def orders(self):
        return self._orders

    @property
    def portins(self):
        return self._portins

    @property
    def portouts(self):
        return self._portouts

    @property
    def sites(self):
        return self._sites

    @property
    def subscriptions(self):
        return self._subscriptions

    @property
    def tnreservation(self):
        return self._tnreservation

    @property
    def users(self):
        return self._users

    @property
    def tn_option_orders(self):
        return self._tn_option_orders

    def __init__(self, parent=None, client=None):
        if client is not None:
            self.id = client.config.account_id
        super().__init__(parent, client)
        AccountData.__init__(self)
        self._available_npa_nxx = AvailableNpaNxx(self, client)
        self._available_numbers = AvailableNumbers(self, client)
        self._disconnected_numbers = DiscNumbers(self, client)
        self._disconnects = Disconnects(self, client)
        self._hosts = SiteHosts(self, client)
        self._import_tn_checker = ImportTnChecker(self, client)
        self._in_service_numbers = InServiceNumbers(self, client)
        self._line_option_orders = LineOptionOrder(self, client)
        self._lnpchecker = LnpChecker(self, client)
        self._orders = Orders(self, client)
        self._portins = PortIns(self, client)
        self._portouts = PortOuts(self, client)
        self._lidbs = Lidbs(self, client)
        self._dldas = Dldas(self, client)
        self._subscriptions = Subscriptions(self, client)
        self._sites = Sites(self, client)
        self._tnreservation = Reservation(self, client)
        self._users = AccountUsers(self, client)
        self._tn_option_orders = TnOptionOrders(self, client)

    def get(self, id=None):
        return self._get_data(id)
