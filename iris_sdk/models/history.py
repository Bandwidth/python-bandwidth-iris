#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.history import HistoryData
from iris_sdk.models.order_history import OrderHistory

XPATH_HISTORY = "/history"

class History(BaseResource, HistoryData):

    """Order history"""

    _save_post = True
    _xpath = XPATH_HISTORY
    _xpath_save = _xpath

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        HistoryData.__init__(self, self)

    def add(self):
        return OrderHistory(self)

    def list(self):
        return self._get_data().order_history