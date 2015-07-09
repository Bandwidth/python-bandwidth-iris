#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.ord.rate_center_search_order import \
    RateCenterSearchOrderMap

class RateCenterSearchOrder(RateCenterSearchOrderMap, BaseData):
    pass