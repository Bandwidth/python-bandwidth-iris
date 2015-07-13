#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.line_option_order_response import LineOptionOrderResponseMap
from iris_sdk.models.line_options import LineOptions

class LineOptionOrderResponseData(LineOptionOrderResponseMap, BaseData):

    def __init__(self, parent=None):
        self.line_options = BaseResourceList(LineOptions, parent=parent)