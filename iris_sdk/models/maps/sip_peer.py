#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class SipPeerMap(BaseMap):

    address = None
    calling_name = None
    description = None
    final_destination_uri = None
    is_default_peer = None
    peer_id = None
    peer_name = None
    short_messaging_protocol = None
    sms_hosts = None
    termination_hosts = None
    voice_hosts = None