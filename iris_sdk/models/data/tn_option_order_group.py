#!/usr/bin/env python
  
from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.tn_option_order_group import TnOptionOrderGroupMap
from iris_sdk.models.data.telephone_number_list import TelephoneNumberList
from iris_sdk.models.data.a2p_settings import A2pSettings

class TnOptionOrderGroupData(TnOptionOrderGroupMap, BaseData):

    def __init__(self, parent=None):
        self.telephone_numbers = TelephoneNumberList()
        self.a2p_settings = A2pSettings()
