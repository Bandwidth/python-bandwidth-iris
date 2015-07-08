#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class OrderAddRateCenterLcaMap(BaseMap):

    back_order_requested = None
    customer_order_id = None
    enable_lca = None
    name = None
    partial_allowed = None
    rate_center_search_and_order_type = None
    site_id = None