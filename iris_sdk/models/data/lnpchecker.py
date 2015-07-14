#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.tn_list import TnList
from iris_sdk.models.maps.lnpchecker import LnpCheckerMap

class LnpCheckerData(LnpCheckerMap, BaseData):

    def __init__(self):
        self.tn_list = TnList()