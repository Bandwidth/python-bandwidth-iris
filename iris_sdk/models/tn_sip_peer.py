#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.maps.sip_peer import SipPeerMap

XML_NAME_SIP_PEER_TN = "SipPeer"
XPATH_SIP_PEER_TN = "/sippeers"

class TnSipPeer(BaseResource, SipPeerMap):

    """SIP peer associated with a telephone number"""

    _node_name = XML_NAME_SIP_PEER_TN
    _xpath = XPATH_SIP_PEER_TN

    @property
    def name(self):
        return self.peer_name
    @name.setter
    def name(self, name):
        self.peer_name = name

    def get(self):
        return self._get_data()