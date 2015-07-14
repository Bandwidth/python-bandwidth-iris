#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource, BaseResourceList
from iris_sdk.models.data.sip_peers import SipPeersData
from iris_sdk.models.sip_peer import SipPeer

XPATH_SIP_PEERS = "/sippeers"

class SipPeers(BaseResource, SipPeersData):

    """Site's SIP peers"""

    _xpath = XPATH_SIP_PEERS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SipPeersData.__init__(self, self)

    def add(self, data=None, save=True):
        sip_peer = SipPeer(self).set_from_dict(data)
        if save:
            sip_peer.save()
        return sip_peer

    def get(self, id):
        return self.add(save=False).get(id)

    def list(self):
        return self._get_data().sip_peer