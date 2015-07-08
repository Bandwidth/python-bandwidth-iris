#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class OrderAddCityMap(BaseMap):

    back_order_requested = None
    city_search_and_order_type = None
    customer_order_id = None
    name = None
    partial_allowed = None
    site_id = None