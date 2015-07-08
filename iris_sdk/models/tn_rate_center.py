#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.tn_rate_center import TnRateCenterData

XML_NAME_RATE_CENTER_TN = "TelephoneNumberDetails"
XPATH_RATE_CENTER_TN = "/ratecenter"

class TnRateCenter(BaseResource, TnRateCenterData):

    """Rate center associated with a telephone number"""

    _node_name = XML_NAME_RATE_CENTER_TN
    _xpath = XPATH_RATE_CENTER_TN

    def get(self):
        return self._get_data()