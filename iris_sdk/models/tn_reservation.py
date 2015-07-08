#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.reservation import Reservation

XML_NAME_RESERVATION_TN = "TNReservation"
XPATH_RESERVATION_TN = "/tnreservation"

class TnReservation(BaseResource, Reservation):

    """Telephone number's reservation"""

    _node_name = XML_NAME_RESERVATION_TN
    _xpath = XPATH_RESERVATION_TN

    def get(self):
        return self._get_data()