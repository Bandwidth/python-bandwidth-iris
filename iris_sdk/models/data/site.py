#!/usr/bin/env python

from iris_sdk.models.data.address import Address
from iris_sdk.models.maps.site import SiteMap

class SiteData(SiteMap):

    address = Address()