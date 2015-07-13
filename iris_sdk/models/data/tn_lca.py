#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResourceSimpleList
from iris_sdk.models.data.location import Location
from iris_sdk.models.data.npanxx_list import NpanxxList
from iris_sdk.models.maps.tn_lca import TnLcaMap

class TnLcaData(TnLcaMap):

    def __init__(self):
        self.listof_npanxx = NpanxxList()
        self.location = Location()