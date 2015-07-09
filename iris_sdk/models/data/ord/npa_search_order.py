#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.ord.npa_search_order import NpaSearchOrderMap

class NpaSearchOrder(NpaSearchOrderMap, BaseData):
    pass