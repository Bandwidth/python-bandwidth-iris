#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.history import HistoryData

XML_NAME_HISTORY = "OrderHistoryWrapper"
XPATH_HISTORY = "/history"

class History(BaseResource, HistoryData):

    """Order history"""

    _node_name = XML_NAME_HISTORY
    _xpath = XPATH_HISTORY

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        HistoryData.__init__(self)

    def list(self):
        return self._get_data().order_history