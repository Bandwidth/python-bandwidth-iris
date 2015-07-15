#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.portouts import PortOutsData

XML_NAME_PORTOUTS = "LNPResponseWrapper"
XPATH_PORTOUTS = "/portouts"

class PortOuts(BaseResource, PortOutsData):

    """Local number portability orders from winning carriers for account"""

    _node_name = XML_NAME_PORTOUTS
    _xpath = XPATH_PORTOUTS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        PortOutsData.__init__(self, self)

    def list(self, params):
        return self._get_data(params=params).lnp_port_info_for_given_status