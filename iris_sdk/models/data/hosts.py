#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.host import Host
from iris_sdk.models.maps.hosts import HostsMap

class Hosts(HostsMap, BaseData):

    @property
    def items(self):
        return self.host.items

    def __init__(self):
        self.host = BaseResourceList(Host)

    def add(self):
        return self.host.add()