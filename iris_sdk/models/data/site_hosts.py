#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.site_host import SiteHost
from iris_sdk.models.maps.site_hosts import SiteHostsMap

class SiteHostsData(SiteHostsMap, BaseData):

    @property
    def items(self):
        return self.site_host.items

    def __init__(self):
        self.site_host = BaseResourceList(SiteHost)