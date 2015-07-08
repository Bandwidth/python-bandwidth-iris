#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class OrderUpdateMap(BaseMap):

    close_order = None
    customer_order_id = None
    name = None