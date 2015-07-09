#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.ord.vanity_search_order import \
    VanitySearchOrderMap

class VanitySearchOrder(VanitySearchOrderMap, BaseData):
    pass