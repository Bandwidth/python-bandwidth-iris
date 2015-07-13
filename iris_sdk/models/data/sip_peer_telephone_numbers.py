#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.sip_peer_telephone_numbers import \
    SipPeerTelephoneNumbersMap
from iris_sdk.models.sip_peer_telephone_number import \
    SipPeerTelephoneNumber

class SipPeerTelephoneNumbers(SipPeerTelephoneNumbersMap, BaseData):

    @property
    def items(self):
        return self.sip_peer_telephone_number.items

    def __init__(self, parent=None):
        self.sip_peer_telephone_number = BaseResourceList(
            SipPeerTelephoneNumber, parent)