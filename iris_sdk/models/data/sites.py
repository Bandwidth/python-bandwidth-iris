#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.sites import SitesMap
from iris_sdk.models.site import Site

class SitesData(SitesMap, BaseData):

    def __init__(self, parent=None):
        self.site = BaseResourceList(Site, self)