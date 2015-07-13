#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.sip_peer_hosts import SipPeerHosts
from iris_sdk.models.maps.site_host import SiteHostMap

class SiteHost(SiteHostMap, BaseData):

    def __init__(self):
        self.sip_peer_hosts = SipPeerHosts()