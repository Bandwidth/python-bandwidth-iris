#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource, BaseResourceList
from iris_sdk.models.sip_peer import SipPeer
from iris_sdk.models.maps.sip_peers import SipPeersMap

XPATH_SIP_PEERS = "/sippeers"

class SipPeers(BaseResource, SipPeersMap):

    """Site's SIP peers"""

    _xpath = XPATH_SIP_PEERS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        self.sip_peer = BaseResourceList(SipPeer, self)

    def add(self):
        return SipPeer(self)

    def get(self, id):
        return self.add().get(id)

    def list(self):
        self._get_data()
        return self.sip_peer