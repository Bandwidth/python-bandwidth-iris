#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.activation_status import ActivationStatus
from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.portin import PortInData
from iris_sdk.models.history import History
from iris_sdk.models.loas import Loas
from iris_sdk.models.notes import Notes
from iris_sdk.models.totals import Totals

XML_NAME_PORTIN = "LnpOrderResponse"
XML_NAME_PORTIN_SAVE = "LnpOrder"
XPATH_PORTIN = "/{}"

class PortIn(BaseResource, PortInData):

    """Local number portability order"""

    _node_name = XML_NAME_PORTIN
    _node_name_save = XML_NAME_PORTIN_SAVE
    _xpath = XPATH_PORTIN

    @property
    def activation_status(self):
        return self._activation_status

    @property
    def history(self):
        return self._history

    @property
    def id(self):
        return self.order_id
    @id.setter
    def id(self, id):
        self.order_id = id

    @property
    def loas(self):
        return self._loas

    @property
    def notes(self):
        return self._notes

    @property
    def totals(self):
        return self._totals

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        PortInData.__init__(self)
        self._activation_status = ActivationStatus(self)
        self._history = History(self)
        self._loas = Loas(self, client)
        self._notes = Notes(self, client)
        self._totals = Totals(self, client)

    def save(self):
        return self._post_data()