#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.maps.site import SiteMap

XML_NAME_SITE_TN = "Site"
XPATH_SITE_TN = "/sites"

class TnSite(BaseResource, SiteMap):

    """Site associated with a telephone number"""

    _node_name = XML_NAME_SITE_TN
    _xpath = XPATH_SITE_TN

    def get(self):
        return self._get_data()