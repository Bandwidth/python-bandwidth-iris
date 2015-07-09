#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.ord.zip_search_order import \
    ZipSearchOrderMap

class ZipSearchOrder(ZipSearchOrderMap, BaseData):
    pass