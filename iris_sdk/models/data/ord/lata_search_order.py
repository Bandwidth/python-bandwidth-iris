#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.ord.lata_search_order import LataSearchOrderMap

class LataSearchOrder(LataSearchOrderMap, BaseData):
    pass