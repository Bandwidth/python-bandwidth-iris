#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.maps.loas import LoasMap

class LoasData(LoasMap, BaseData):

    def __init__(self):
        self.file_names = BaseResourceSimpleList()