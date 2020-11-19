#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super
from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.import_tn_checker import ImportTnCheckerData
from iris_sdk.models.import_tn_checker_response import ImportTnCheckerResponse

XML_NAME_IMPORTTN_CHECKER = "ImportTnCheckerPayload"
XPATH_IMPORTTN_CHECKER = "/importTnChecker"

class ImportTnChecker(BaseResource, ImportTnCheckerData):

    """Request portability information for hosted messaging on a set of TNs"""

    _save_post = True
    _node_name = XML_NAME_IMPORTTN_CHECKER
    _xpath = XPATH_IMPORTTN_CHECKER

    def __call__(self, numbers):
        self.clear()
        self.telephone_numbers.items.extend(numbers)
        return self._post_data(ImportTnCheckerResponse())

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        ImportTnCheckerData.__init__(self)
