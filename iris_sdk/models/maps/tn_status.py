#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class TnStatusMap(BaseMap):

    account_id = None
    last_modified_date = None
    order_create_date = None
    order_id = None
    order_type = None
    status = None