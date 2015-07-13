#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.sip_peer import SipPeerData
from iris_sdk.models.data.address import Address
from iris_sdk.models.data.calling_name import CallingName
from iris_sdk.models.data.hosts import Hosts
from iris_sdk.models.data.termination_hosts import TerminationHosts
from iris_sdk.models.maps.sip_peer import SipPeerMap
from iris_sdk.models.movetns import Movetns
from iris_sdk.models.sip_peer_tns import SipPeerTns
from iris_sdk.models.sip_peer_totaltns import SipPeerTotaltns

XPATH_SIP_PEER = "/{}"

class SipPeer(BaseResource, SipPeerData):

    """Site SIP peer"""

    _xpath = XPATH_SIP_PEER

    @property
    def id(self):
        return self.peer_id
    @id.setter
    def id(self, id):
        self.peer_id = id

    @property
    def movetns(self):
        return self._movetns

    @property
    def tns(self):
        return self._tns

    @property
    def totaltns(self):
        return self._totaltns

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SipPeerData.__init__(self)
        self._movetns = Movetns(self, client)
        self._tns = SipPeerTns(self, client)
        self._totaltns = SipPeerTotaltns(self, client)

    def get(self, id=None):
        return self._get_data(id)