#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.ord.state_search_order import \
    StateSearchOrderMap

class StateSearchOrder(StateSearchOrderMap, BaseData):
    pass