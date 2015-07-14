#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class LnpRateCenterMap(BaseMap):

    city = None
    lata = None
    rate_center = None
    state = None
    tiers = None
    tn_list = None