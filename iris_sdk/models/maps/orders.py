#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class OrdersMap(BaseMap):

    links = None
    order_id_user_id_date = None
    total_count = None