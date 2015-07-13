#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.totals import TotalsMap

class TotalsData(TotalsMap, BaseData):
    pass