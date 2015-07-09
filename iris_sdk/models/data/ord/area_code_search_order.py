#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.ord.area_code_search_order import \
    AreaCodeSearchOrderMap

class AreaCodeSearchOrder(AreaCodeSearchOrderMap, BaseData):
    pass