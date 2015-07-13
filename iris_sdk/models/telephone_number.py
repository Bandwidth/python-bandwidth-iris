#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.telephone_number import TelephoneNumberData
from iris_sdk.models.tn_history import TnHistory
from iris_sdk.models.tn_lata import TnLata
from iris_sdk.models.tn_lca import TnLca
from iris_sdk.models.tn_rate_center import TnRateCenter
from iris_sdk.models.tn_reservation import TnReservation
from iris_sdk.models.tn_sip_peer import TnSipPeer
from iris_sdk.models.tn_site import TnSite
from iris_sdk.models.tndetails import Tndetails

XML_NAME_TN = "TelephoneNumberResponse"
XPATH_TN = "/{}"

class TelephoneNumber(BaseResource, TelephoneNumberData):

    """Telephone number"""

    _node_name = XML_NAME_TN
    _xpath = XPATH_TN

    @property
    def history(self):
        return self._history

    @property
    def id(self):
        return self.full_number
    @id.setter
    def id(self, id):
        self.full_number = id

    @property
    def lca(self):
        return self._lca

    @property
    def sip_peer(self):
        return self._sip_peer

    @property
    def site(self):
        return self._site

    @property
    def tndetails(self):
        return self._tndetails

    @property
    def tn_lata(self):
        return self._lata

    @property
    def tn_rate_center(self):
        return self._rate_center

    @property
    def tnreservation(self):
        return self._tnreservation

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        self._history = TnHistory(self, client)
        self._lata = TnLata(self, client)
        self._lca = TnLca(self, client)
        self._rate_center = TnRateCenter(self, client)
        self._sip_peer = TnSipPeer(self, client)
        self._site = TnSite(self, client)
        self._tndetails = Tndetails(self, client)
        self._tnreservation = TnReservation(self, client)

    def get(self, id=None):
        return self._get_data(id)