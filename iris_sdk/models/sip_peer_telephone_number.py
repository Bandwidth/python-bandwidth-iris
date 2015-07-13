#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.sip_peer_telephone_number import \
    SipPeerTelephoneNumberData

XPATH_SIP_PEER_TN = "/{}"

class SipPeerTelephoneNumber(BaseResource, SipPeerTelephoneNumberData):

    """Sip peer telephone number"""

    _xpath = XPATH_SIP_PEER_TN

    @property
    def id(self):
        return self.full_number
    @id.setter
    def id(self, id):
        self.full_number = id

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SipPeerTelephoneNumberData.__init__(self)

    def get(self, id=None):
        return self._get_data(id)