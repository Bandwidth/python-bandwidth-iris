#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.line_option_order_response import LineOptionOrderResponseMap
from iris_sdk.models.data.line_options import LineOptionsData

class LineOptionOrderResponseData(LineOptionOrderResponseMap, BaseData):

    def __init__(self):
        self.line_options = BaseResourceList(LineOptionsData)