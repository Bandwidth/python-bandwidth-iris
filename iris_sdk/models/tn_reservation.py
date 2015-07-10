#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.reservation import ReservationData

XML_NAME_RESERVATION_TN = "TNReservation"
XPATH_RESERVATION_TN = "/tnreservation"

class TnReservation(BaseResource, ReservationData):

    """Telephone number's reservation"""

    _node_name = XML_NAME_RESERVATION_TN
    _xpath = XPATH_RESERVATION_TN

    @property
    def reservation_id(self):
        return self.id
    @reservation_id.setter
    def reservation_id(self, reservation_id):
        self.id = reservation_id

    def get(self):
        return self._get_data()