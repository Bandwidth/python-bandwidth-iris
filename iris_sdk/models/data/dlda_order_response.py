#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.dlda import Dlda
from iris_sdk.models.maps.dlda_order_response import DldaOrderResponseMap

class DldaOrderResponseData(DldaOrderResponseMap, BaseData):

    def __init__(self):
        self.dlda_order = Dlda()