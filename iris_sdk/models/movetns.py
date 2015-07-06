#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BASE_ID_SKIP, BaseResource, \
    BaseResourceList
from iris_sdk.models.data.movetns import MovetnsData

XML_NAME_MOVETNS = "SipPeerTelephoneNumbers"
XPATH_MOVETNS = "/movetns"

class Movetns(BaseResource, MovetnsData):

    """Moving telephone numbers across SIP peers"""

    _node_name = XML_NAME_MOVETNS
    _xpath = XPATH_MOVETNS

    @property
    def items(self):
        return self.full_number

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        MovetnsData.__init__(self)
        self.id = BASE_ID_SKIP

    def add(self, full_number):
        self.full_number.append(full_number)

    def clear(self):
        del self.full_number[:]