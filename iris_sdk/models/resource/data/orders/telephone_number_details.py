#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.resource.data.orders.cities import Cities
from iris_sdk.models.resource.data.orders.rate_centers import RateCenters
from iris_sdk.models.resource.data.orders.states import States
from iris_sdk.models.resource.data.orders.tiers import Tiers
from iris_sdk.models.resource.data.orders.vendors import Vendors

class TelephoneNumberDetailsData(object):

    @property
    def cities(self):
        return self._cities

    @property
    def cities_list(self):
        return self.cities.city_with_count.items

    @property
    def rate_centers(self):
        return self._rate_centers

    @property
    def rate_centers_list(self):
        return self.rate_centers.rate_center_with_count.items

    @property
    def states(self):
        return self._states

    @property
    def states_list(self):
        return self.states.state_with_count.items

    @property
    def tiers(self):
        return self._tiers

    @property
    def tiers_list(self):
        return self.tiers.tier_with_count.items

    @property
    def vendors(self):
        return self._vendors

    @property
    def vendors_list(self):
        return self.vendors.vendor_with_count.items

class TelephoneNumberDetails(TelephoneNumberDetailsData):

    def __init__(self):
        self._cities = Cities()
        self._rate_centers = RateCenters()
        self._states = States()
        self._tiers = Tiers()
        self._vendors = Vendors()
