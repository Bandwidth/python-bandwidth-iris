#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.tn_history import TnHistoryData

XML_NAME_HISTORY_TN = "TelephoneNumberStatuses"
XPATH_HISTORY_TN = "/history"

class TnHistory(BaseResource, TnHistoryData):

    """Telephone number history"""

    _node_name = XML_NAME_HISTORY_TN
    _xpath = XPATH_HISTORY_TN

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        TnHistoryData.__init__(self)

    def list(self):
        return self._get_data().telephone_number_status