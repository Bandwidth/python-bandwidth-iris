#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.sip_peers import SipPeersMap
from iris_sdk.models.sip_peer import SipPeer

class SipPeersData(SipPeersMap, BaseData):

    def __init__(self, parent=None):
        self.sip_peer = BaseResourceList(SipPeer, self)