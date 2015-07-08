#!/usr/bin/env python

from iris_sdk.models.data.address import Address
from iris_sdk.models.data.calling_name import CallingName
from iris_sdk.models.data.hosts import Hosts
from iris_sdk.models.data.termination_hosts import TerminationHosts
from iris_sdk.models.maps.sip_peer import SipPeerMap

class SipPeerData(SipPeerMap):

    @property
    def name(self):
        return self.peer_name
    @name.setter
    def name(self, name):
        self.peer_name = name

    @property
    def peer_id(self):
        return self.id
    @peer_id.setter
    def peer_id(self, peer_id):
        self.id = peer_id

    def __init__(self):
        self.address = Address()
        self.calling_name = CallingName()
        self.sms_hosts = Hosts()
        self.termination_hosts = TerminationHosts()
        self.voice_hosts = Hosts()