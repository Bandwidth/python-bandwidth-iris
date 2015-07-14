#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.links import Links
from iris_sdk.models.maps.lidbs import LidbsMap
from iris_sdk.models.lidb import Lidb

class LidbsData(LidbsMap, BaseData):

    def __init__(self, parent=None):
        self.lidb_tn_groups = BaseResourceList(Lidb, parent)