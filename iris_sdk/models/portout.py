#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.portin import PortInData
from iris_sdk.models.notes import Notes
from iris_sdk.models.totals import Totals

XML_NAME_PORTOUT = "LnpOrderResponse"
XPATH_PORTOUT = "/{}"

class PortOut(BaseResource, PortInData):

    """Local number portability order from a winning carrier"""

    _node_name = XML_NAME_PORTOUT
    _xpath = XPATH_PORTOUT

    @property
    def notes(self):
        return self._notes

    @property
    def totals(self):
        return self._totals

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        PortInData.__init__(self)
        self._notes = Notes(self)
        self._totals = Totals(self, client)