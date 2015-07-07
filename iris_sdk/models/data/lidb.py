#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.lidb import LidbMap

class Lidb(LidbMap, BaseData):
    pass