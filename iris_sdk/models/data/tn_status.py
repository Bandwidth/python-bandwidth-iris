#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.tn_status import TnStatusMap

class TnStatus(TnStatusMap, BaseData):
    pass