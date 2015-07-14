#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.lidb_tn_group import LidbTnGroupMap
from iris_sdk.models.data.telephone_number_list import TelephoneNumberList
f
class LidbTnGroupData(LidbTnGroupMap, BaseData):

    def __init__(self):
        self.telephone_numbers = TelephoneNumberList()