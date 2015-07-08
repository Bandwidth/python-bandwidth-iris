#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.include.xml_consts import XML_PARAM_TN_DETAIL, XML_TRUE
from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.rate_centers import RateCentersData

XML_NAME_RATE_CENTERS = "RateCenterResponse"
XPATH_RATE_CENTERS = "/ratecenters"

class RateCenters(BaseResource, RateCentersData):

    """Rate centers directory"""

    _node_name = XML_NAME_RATE_CENTERS
    _xpath = XPATH_RATE_CENTERS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        RateCentersData.__init__(self)

    def list(self, params):
        return self._get_data(params=params).rate_centers.rate_center