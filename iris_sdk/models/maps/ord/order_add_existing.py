#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class OrderAddExistingMap(BaseMap):

    customer_order_id = None
    existing_telephone_number_order_type = None
    name = None
    partial_allowed = None
    peer_id = None
    reservation_id_list = None
    site_id = None