#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.line_option_order import LineOptionOrderMap
from iris_sdk.models.tn_line_options import TnLineOptions

class LineOptionOrderData(LineOptionOrderMap, BaseData):

    def __init__(self, parent=None):
        self.tn_line_options = BaseResourceList(TnLineOptions, parent)