#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.reservation import ReservationData

XML_NAME_RESERVATION = "Reservation"
XPATH_RESERVATION = "/tnreservation/{}"
XPATH_RESERVATION_SAVE = "/tnreservation"

class Reservation(BaseResource, ReservationData):

    """Account's telephone number reservation"""

    _node_name = XML_NAME_RESERVATION
    _save_post = True
    _xpath = XPATH_RESERVATION
    _xpath_save = XPATH_RESERVATION_SAVE

    @property
    def reservation_id(self):
        return self.id
    @reservation_id.setter
    def reservation_id(self, reservation_id):
        self.id = reservation_id

    def get(self, id=None):
        return self._get_data(id)