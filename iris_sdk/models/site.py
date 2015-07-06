#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource, BaseResourceList
from iris_sdk.models.data.site import SiteData
from iris_sdk.models.sip_peers import SipPeers

XPATH_SITE = "/{}"

class Site(BaseResource, SiteData):

    """Account site"""

    _xpath = XPATH_SITE

    @property
    def sip_peers(self):
        return self._sip_peers

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SiteData.__init__(self)
        self._sip_peers = SipPeers(self, client)

    def get(self, id):
        return self.get_data(id)