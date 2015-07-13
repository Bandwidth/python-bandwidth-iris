#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.cities_short_list import CitiesShortList
from iris_sdk.models.data.local_rate_center_list import LocalRateCenterList
from iris_sdk.models.data.npanxx_list import NpanxxList
from iris_sdk.models.data.tier_list import TierList
from iris_sdk.models.data.zip_code_list import ZipCodeList
from iris_sdk.models.maps.rate_center import RateCenterMap

class RateCenterData(RateCenterMap, BaseData):

    def __init__(self):
        self.cities = CitiesShortList()
        self.local_rate_centers = LocalRateCenterList()
        self.npa_nxx_xs = NpanxxList()
        self.tiers = TierList()
        self.zip_codes = ZipCodeList()