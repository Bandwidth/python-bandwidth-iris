#!/usr/bin/env python

from iris_sdk.models.data.address import Address
from iris_sdk.models.maps.site import SiteMap

class SiteData(SiteMap):

    def __init__(self):
        self.address = Address()