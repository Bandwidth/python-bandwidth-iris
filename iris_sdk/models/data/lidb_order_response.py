#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.lidb import Lidb
from iris_sdk.models.maps.lidb_order_response import LidbOrderResponseMap

class LidbOrderResponseData(LidbOrderResponseMap, BaseData):

    def __init__(self):
        self.lidb_order = Lidb()