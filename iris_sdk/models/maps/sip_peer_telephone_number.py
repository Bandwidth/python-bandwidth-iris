#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class SipPeerTelephoneNumberMap(BaseMap):

    call_forward = None
    calling_name_display = None
    full_number = None
    number_format = None
    rewrite_user = None
    rpid_format = None
    tn_attributes = None