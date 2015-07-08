#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class CityMap(BaseMap):

    city = None
    name = None
    rc_abbreviation = None