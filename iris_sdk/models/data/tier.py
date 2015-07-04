#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.tier import TierMap

class Tier(TierMap, BaseData):
    pass