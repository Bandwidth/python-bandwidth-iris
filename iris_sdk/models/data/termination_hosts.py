#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.host import Host
from iris_sdk.models.maps.termination_hosts import TerminationHostsMap

class TerminationHosts(TerminationHostsMap, BaseData):

    @property
    def items(self):
        return self.termination_host.items

    def __init__(self):
        self.termination_host = BaseResourceList(Host)

    def add(self):
        return self.termination_host.add()