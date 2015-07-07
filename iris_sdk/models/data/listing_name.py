#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.listing_name import ListingNameMap

class ListingName(ListingNameMap, BaseData):
    pass