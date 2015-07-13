#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.npa_nxx import NpaNxxMap

class NpaNxx(NpaNxxMap, BaseData):
    pass