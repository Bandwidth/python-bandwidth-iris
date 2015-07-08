#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class ReservationMap(BaseMap):

    account_id = None
    reservation_id = None
    reservation_expires = None
    reserved_tn = None