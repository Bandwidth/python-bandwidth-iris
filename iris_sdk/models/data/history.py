#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.order_history import OrderHistoryData
from iris_sdk.models.maps.history import HistoryMap

class HistoryData(HistoryMap, BaseData):

    def __init__(self):
        self.order_history = BaseResourceList(OrderHistoryData)