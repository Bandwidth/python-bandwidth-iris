#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.site_hosts import SiteHostsData

XML_NAME_SITE_HOSTS = "SiteHosts"
XPATH_SITE_HOSTS = "/hosts"

class SiteHosts(BaseResource, SiteHostsData):

    """Sites hosts list"""

    _node_name = XML_NAME_SITE_HOSTS
    _xpath = XPATH_SITE_HOSTS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SiteHostsData.__init__(self)

    def list(self, params=None):
        return self._get_data(params=params).site_host