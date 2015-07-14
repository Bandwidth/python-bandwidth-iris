#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.feature_lidb import FeatureLidbMap

class FeatureLidb(FeatureLidbMap, BaseData):
    pass