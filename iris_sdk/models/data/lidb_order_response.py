#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.lidb_order_response import LidbOrderResponseMap
from iris_sdk.models.data.response_status import ResponseStatus

class LidbOrderResponseData(LidbOrderResponseMap, BaseData):

    def __init__(self):
        self.response_status = ResponseStatus()