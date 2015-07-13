#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.sip_peer_telephone_numbers import \
    SipPeerTelephoneNumbers
from iris_sdk.models.maps.sip_peer_tns import SipPeerTnsMap

class SipPeerTnsData(SipPeerTnsMap, BaseData):

    def __init__(self, parent=None):
        self.sip_peer_telephone_numbers = SipPeerTelephoneNumbers(parent)