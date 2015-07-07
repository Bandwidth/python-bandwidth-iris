#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.telephone_number import TelephoneNumberData

XML_NAME_TN = "TelephoneNumberResponse"
XPATH_TN = "/{}"
XPATH_TN_DETAILS = "/tndetails"

class TelephoneNumber(BaseResource, TelephoneNumberData):

    """Telephone number"""

    _node_name = XML_NAME_TN
    _xpath = XPATH_TN

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        TelephoneNumberData.__init__(self)

    def get(self, id=None):
        new_id = (id or self.id)
        self._get_data(new_id)
        self.id = new_id
        return self

    def tndetails(self, id=None):
        return self._get_data(id=id, xpath=XPATH_TN_DETAILS)