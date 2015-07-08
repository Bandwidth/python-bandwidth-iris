#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.tndetails import TndetailsData

XML_NAME_TNDETAILS = "TelephoneNumberDetails"
XPATH_TNDETAILS = "/tndetails"

class Tndetails(BaseResource, TndetailsData):

    """Telephone number details"""

    _node_name = XML_NAME_TNDETAILS
    _xpath = XPATH_TNDETAILS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        TndetailsData.__init__(self)

    def get(self):
        return self._get_data()