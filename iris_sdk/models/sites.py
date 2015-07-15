#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource, BaseResourceList
from iris_sdk.models.data.sites import SitesData
from iris_sdk.models.site import Site

XPATH_SITES = "/sites"

class Sites(BaseResource, SitesData):

    """Account sites"""

    _xpath = XPATH_SITES

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SitesData.__init__(self, self)

    def add(self, data=None, save=True):
        site = Site(self).set_from_dict(data)
        if save and (data is not None):
            site.save()
        return site

    def get(self, id):
        return self.add(save=False).get(id)

    def list(self):
        return self._get_data().site