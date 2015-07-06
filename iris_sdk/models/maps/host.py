#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class HostMap(BaseMap):

    customer_traffic_allowed = None
    data_allowed = None
    host_name = None
    port = None