#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.data.city import City
from iris_sdk.models.data.local_rate_center import LocalRateCenter
from iris_sdk.models.data.npanxx import Npanxx
from iris_sdk.models.data.tier import Tier
from iris_sdk.models.data.zip_code import ZipCode
from iris_sdk.models.maps.rate_center import RateCenterMap

class RateCenterData(RateCenterMap, BaseData):

    def __init__(self):
        self.cities = BaseResourceSimpleList(City)
        self.local_rate_centers = BaseResourceSimpleList(LocalRateCenter)
        self.npa_nxx_xs = BaseResourceSimpleList(Npanxx)
        self.tiers = BaseResourceSimpleList(Tier)
        self.zip_codes = BaseResourceSimpleList(ZipCode)