#!/usr/bin/env python
  
from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.tn_option_order_group import TnOptionOrderGroupMap
from iris_sdk.models.data.telephone_numbers import TelephoneNumbers
from iris_sdk.models.data.a2p_settings import A2pSettings

class TnOptionOrderGroupData(TnOptionOrderGroupMap, BaseData):

    def __init__(self, parent=None):
        self.telephone_numbers = TelephoneNumbers()
        self.a2p_settings = A2pSettings()
