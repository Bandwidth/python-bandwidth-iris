#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.lnpchecker import LnpCheckerData
from iris_sdk.data.lnpchecker_response import LnpCheckerResponse

XPATH_LNP_CHECKER = "/lnpchecker"

class LnpChecker(BaseResource, LnpCheckerData):

    """Check local number portability"""

    _xpath = XPATH_LNP_CHECKER

    @property
    def id(self):
        return self.order_id
    @id.setter
    def id(self, id):
        self.order_id = id

    def __call__(self):
        return self._post_data(LnpCheckerResponse())

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LnpCheckerData.__init__(self)