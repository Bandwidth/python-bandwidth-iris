#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.lnp_loosing_carriers import LnpLosingCarriers
from iris_sdk.models.data.lnp_rate_center_list import LnpRateCenterList
from iris_sdk.models.data.tn_list import TnList
from iris_sdk.models.maps.lnpchecker_response import LnpCheckerResponse

class LnpCheckerResponse(LnpCheckerMap, BaseData):

    def __init__(self):
        self.partner_supported_rate_centers = LnpRateCenterList()
        self.portable_numbers = TnList()
        self.supported_losing_carriers = LnpLosingCarriers()
        self.supported_rate_centers = LnpRateCenterList()
        self.unsupported_rate_centers = LnpRateCenterList()