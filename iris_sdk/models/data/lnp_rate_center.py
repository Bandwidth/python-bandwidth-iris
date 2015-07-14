#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.tier_list import TierList
from iris_sdk.models.data.tn_list import TnList
from iris_sdk.models.maps.lnp_rate_center import LnpRateCenterMap

class LnpRateCenter(LnpRateCenterMap, BaseData):

    def __init__(self):
        self.tiers = TierList()
        self.tn_list = TnList()