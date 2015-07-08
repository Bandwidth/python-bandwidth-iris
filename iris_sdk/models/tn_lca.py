#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.tn_lca import TnLcaData

XML_NAME_LCA_TN = "SearchResult"
XPATH_LCA_TN = "/lca"

class TnLca(BaseResource, TnLcaData):

    """LCAs associated with a telephone number"""

    _node_name = XML_NAME_LCA_TN
    _xpath = XPATH_LCA_TN

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        TnLcaData.__init__(self)

    def get(self):
        return self._get_data()