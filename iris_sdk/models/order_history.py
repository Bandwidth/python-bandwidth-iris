#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.order_history import OrderHistoryData

XPATH_ORDER_HISTORY = ""

class OrderHistory(BaseResource, OrderHistoryData):

    """Order history"""

    _save_post = True
    _xpath = XPATH_ORDER_HISTORY
    _xpath_save = _xpath

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)

    def save(self):
        self.user_id = self.client.config.username
        self._save()