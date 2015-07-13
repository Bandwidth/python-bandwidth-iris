#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.sip_peer_totaltns import SipPeerTotaltnsData

XML_NAME_TOTALTNS_SIP_PEER = "SipPeerTelephoneNumbersCounts"
XPATH_TOTALTNS_SIP_PEER = "/totaltns"

class SipPeerTotaltns(BaseResource, SipPeerTotaltnsData):

    """Total telephone numbers count for a sip peer"""

    _node_name = XML_NAME_TOTALTNS_SIP_PEER
    _xpath = XPATH_TOTALTNS_SIP_PEER

    def get(self, params=None):
        return self._get_data(params=params)