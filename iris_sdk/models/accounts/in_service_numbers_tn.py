#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResource

XPATH_IN_SERVICE_NUMBERS_TN = "/{}"

class Tn(BaseResource):

    """In-service telephone number verification."""

    _xpath = XPATH_IN_SERVICE_NUMBERS_TN

    def get(self, number):
        return self.get_status(id=number)