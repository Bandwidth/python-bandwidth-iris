#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class ActivationStatusMap(BaseMap):

    activated_telephone_numbers_list = None
    auto_activation_date = None
    not_yet_activated_telephone_numbers_list = None