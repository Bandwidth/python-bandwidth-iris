#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource, BaseResourceList
from iris_sdk.models.site import Site
from iris_sdk.models.maps.sites import SitesMap

XPATH_SITES = "/sites"

class Sites(BaseResource, SitesMap):

    """Account sites"""

    _xpath = XPATH_SITES

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        self.site = BaseResourceList(Site, self)

    def add(self):
        return Site(self)

    def get(self, id):
        return self.add().get(id)

    def list(self):
        self.get_data()
        return self.site