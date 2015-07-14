#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.lnpchecker import LnpCheckerData
from iris_sdk.models.lnpchecker_response import LnpCheckerResponse

XML_NAME_LNP_CHECKER = "NumberPortabilityRequest"
XPATH_LNP_CHECKER = "/lnpchecker"

class LnpChecker(BaseResource, LnpCheckerData):

    """Check local number portability"""

    _save_post = True
    _node_name = XML_NAME_LNP_CHECKER
    _xpath = XPATH_LNP_CHECKER

    def __call__(self, numbers, params=None):
        self.clear()
        self.tn_list.items.extend(numbers)
        return self._post_data(LnpCheckerResponse(), params)

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LnpCheckerData.__init__(self)