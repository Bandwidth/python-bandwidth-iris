#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class OrderAddZipMap(BaseMap):

    back_order_requested = None
    customer_order_id = None
    name = None
    partial_allowed = None
    site_id = None
    zip_search_and_order_type = None