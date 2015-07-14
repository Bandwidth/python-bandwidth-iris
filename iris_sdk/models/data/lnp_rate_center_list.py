#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.lnp_rate_center import LnpRateCenter
from iris_sdk.models.maps.lnp_rate_center_list import LnpRateCenterListMap

class LnpRateCenterList(LnpRateCenterListMap, BaseData):

    @property
    def items(self):
        return self.rate_center_group.items

    def __init__(self):
        self.rate_center_group = BaseResourceList(LnpRateCenter)