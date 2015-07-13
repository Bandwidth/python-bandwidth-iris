#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.sip_peer_tns import SipPeerTnsData
from iris_sdk.models.sip_peer_telephone_number import \
    SipPeerTelephoneNumber

XML_NAME_SIP_PEER_TNS = "SipPeerTelephoneNumbersResponse"
XPATH_SIP_PEER_TNS = "/tns"

class SipPeerTns(BaseResource, SipPeerTnsData):

    """SIP peers telephone numbers"""

    _node_name = XML_NAME_SIP_PEER_TNS
    _xpath = XPATH_SIP_PEER_TNS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SipPeerTnsData.__init__(self, self)

    def get(self, id):
        retutn = SipPeerTelephoneNumber(self).get(id)

    def list(self):
        return self._get_data().sip_peer_telephone_numbers.\
            sip_peer_telephone_number