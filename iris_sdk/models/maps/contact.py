#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class ContactMap(BaseMap):

    email = None
    first_name = None
    last_name = None
    phone = None