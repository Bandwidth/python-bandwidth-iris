#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class PortInsMap(BaseMap):

    links = None
    lnp_port_info_for_given_status = None
    total_count = None