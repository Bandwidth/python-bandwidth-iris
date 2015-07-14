#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.lnpchecker_response import LnpCheckerResponseData

XML_NAME_LNP_CHECKER_RESPONSE = "NumberPortabilityResponse"

class LnpCheckerResponse(BaseResource, LnpCheckerResponseData):

    """Local number portability check response"""

    _node_name = XML_NAME_LNP_CHECKER_RESPONSE

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LnpCheckerResponseData.__init__(self)