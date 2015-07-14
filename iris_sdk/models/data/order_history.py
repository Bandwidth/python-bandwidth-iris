#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.order_history import OrderHistoryMap

class OrderHistoryData(OrderHistoryMap, BaseData):
    pass