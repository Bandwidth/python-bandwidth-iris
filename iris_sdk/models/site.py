#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.site import SiteData

#from iris_sdk.models.resource.orders import Orders

XPATH_SITE = "/sites/{}"

class Site(SiteData, BaseResource):

    """Account site"""

    _xpath = XPATH_SITE

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        #self._orders = Orders(client, self._xpath)

    def get(self, id):
        return self.get_data(id)