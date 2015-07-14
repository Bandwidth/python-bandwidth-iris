#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.wireless_info import WirelessInfoMap

class WirelessInfo(WirelessInfoMap, BaseData):
    pass