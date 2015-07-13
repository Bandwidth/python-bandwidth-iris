#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource, BaseResourceList
from iris_sdk.models.data.movetns import MovetnsData

XML_NAME_MOVETNS = "SipPeerTelephoneNumbers"
XPATH_MOVETNS = "/movetns"

class Movetns(BaseResource, MovetnsData):

    """Moving telephone numbers across SIP peers"""

    _node_name = XML_NAME_MOVETNS
    _save_post = True
    _xpath = XPATH_MOVETNS

    def __call__(self):
        self.save()

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        MovetnsData.__init__(self)