#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.error_list import ErrorList
from iris_sdk.models.data.full_numbers import FullNumbers
from iris_sdk.models.data.completed_numbers import CompletedNumbers
from iris_sdk.models.maps.order_response import OrderResponseMap

class OrderResponseData(OrderResponseMap, BaseData):

    def __init__(self):
        self.completed_numbers = CompletedNumbers()
        self.error_list = ErrorList()
        self.failed_numbers = FullNumbers()
