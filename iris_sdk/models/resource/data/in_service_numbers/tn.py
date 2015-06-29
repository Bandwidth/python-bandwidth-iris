#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource

XPATH_IN_SERVICE_NUMBERS_TN = "/{}"

class TN(BaseResource):

    """In-service telephone number verification."""

    _xpath = XPATH_IN_SERVICE_NUMBERS_TN

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)

    def get(self, number):
        return self.get_status(id=number)