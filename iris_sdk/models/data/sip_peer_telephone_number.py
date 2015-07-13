#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.tn_attributes import TnAttributes
from iris_sdk.models.maps.sip_peer_telephone_number import \
    SipPeerTelephoneNumberMap

class SipPeerTelephoneNumberData(SipPeerTelephoneNumberMap, BaseData):

    def __init__(self):
        self.tn_attributes = TnAttributes()