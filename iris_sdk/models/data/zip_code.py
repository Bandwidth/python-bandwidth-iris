#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.zip_code import ZipCodeMap

class ZipCode(ZipCodeMap, BaseData):
    pass