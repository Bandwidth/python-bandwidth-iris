#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.rate_center import RateCenterData

XML_NAME_COVERED_RATE_CENTER = "CoveredRateCenter"
XPATH_COVERED_RATE_CENTER = "/{}"

class RateCenter(BaseResource, RateCenterData):

    """Rate Center"""

    _node_name = XML_NAME_COVERED_RATE_CENTER
    _xpath = XPATH_COVERED_RATE_CENTER

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        RateCenterData.__init__(self)

    def get(self, id=None):
        new_id = (id or self.id)
        self._get_data(new_id)
        self.id = new_id
        return self