#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.covered_rate_centers import CoveredRateCentersData
from iris_sdk.models.rate_center import RateCenter

XPATH_COVERED_RATE_CENTERS = "/coveredratecenters"

class CoveredRateCenters(BaseResource, CoveredRateCentersData):

    """Covered rate centers"""

    _xpath = XPATH_COVERED_RATE_CENTERS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        CoveredRateCentersData.__init__(self, self)

    def get(self, id):
        return RateCenter(self).get(id)

    def list(self, params):
        return self._get_data(params=params).covered_rate_center