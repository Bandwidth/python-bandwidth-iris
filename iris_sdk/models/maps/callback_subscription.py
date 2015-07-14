#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class CallbackSubscriptionMap(BaseMap):

    url = None
    user = None
    expiry = None
    status = None