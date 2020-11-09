#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super
from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.import_tn_checker_response import ImportTnCheckerResponseData

XML_NAME_IMPORTTN_CHECKER_RESPONSE = "ImportTnCheckerResponse"

class ImportTnCheckerResponse(BaseResource, ImportTnCheckerResponseData):

    """Import TN Checker Response"""

    _node_name = XML_NAME_IMPORTTN_CHECKER_RESPONSE

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        ImportTnCheckerResponseData.__init__(self)
