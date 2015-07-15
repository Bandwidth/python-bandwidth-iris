#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList, \
    BaseResourceSimpleList
from iris_sdk.models.data.file_data import FileData
from iris_sdk.models.maps.loas import LoasMap

class LoasData(LoasMap, BaseData):

    def __init__(self):
        self.file_data = BaseResourceList(FileData)
        self.file_names = BaseResourceSimpleList()