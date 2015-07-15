#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.file_meta_data import FileMetaDataData
from iris_sdk.models.maps.file_data import FileDataMap

class FileData(FileDataMap, BaseData):

    def __init__(self):
        self.file_meta_data = FileMetaDataData()