#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class LnpCheckerResponseMap(BaseMap):

    partner_supported_rate_centers = None
    portable_numbers = None
    supported_losing_carriers = None
    supported_rate_centers = None
    unsupported_rate_centers = None