#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.losing_carrier_tn_list import LosingCarrierTnList
from iris_sdk.models.maps.lnp_losing_carriers import LnpLosingCarriersMap

class LnpLosingCarriers(LnpLosingCarriersMap, BaseData):

    def __init__(self):
        self.losing_carrier_tn_list = LosingCarrierTnList()