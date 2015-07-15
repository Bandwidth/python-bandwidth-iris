#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.file_meta_data import FileMetaDataMap

class FileMetaDataData(FileMetaDataMap, BaseData):
    pass