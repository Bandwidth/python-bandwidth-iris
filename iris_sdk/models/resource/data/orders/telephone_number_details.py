#!/usr/bin/env python

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
    def rate_centers(self):
        return self._rate_centers

    @property
    def states(self):
        return self._states

    @property
    def tiers(self):
        return self._tiers

    @property
    def vendors(self):
        return self._vendors

class TelephoneNumberDetails(TelephoneNumberDetailsData):

    def __init__(self):
        self._cities = Cities()
        self._rate_centers = RateCenters()
        self._states = States()
        self._tiers = Tiers()
        self._vendors = Vendors()
