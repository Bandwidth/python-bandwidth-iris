#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.host import HostMap

class Host(HostMap, BaseData):
    pass