#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.order_history import OrderHistory
from iris_sdk.models.maps.history import HistoryMap

class HistoryData(HistoryMap, BaseData):

    def __init__(self, parent=None):
        self.order_history = BaseResourceList(OrderHistory, parent)