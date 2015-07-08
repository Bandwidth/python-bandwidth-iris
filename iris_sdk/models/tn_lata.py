#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.maps.lata import LataMap

XML_NAME_LATA_TN = "TelephoneNumberDetails"
XPATH_LATA_TN = "/lata"

class TnLata(BaseResource, LataMap):

    """Lata associated with a telephone number"""

    _node_name = XML_NAME_LATA_TN
    _xpath = XPATH_LATA_TN

    def get(self):
        return self._get_data()