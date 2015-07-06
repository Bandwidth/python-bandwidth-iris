#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.movetns import MovetnsMap

class MovetnsData(MovetnsMap, BaseData):

    def __init__(self):
        self.full_number = []