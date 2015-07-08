#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class AccountUserMap(BaseMap):

    email_address = None
    first_name = None
    last_name = None
    roles = None
    telephone_number = None
    username = None