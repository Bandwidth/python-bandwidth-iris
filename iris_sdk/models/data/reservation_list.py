#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.data.reservation import ReservationData
from iris_sdk.models.maps.reservation_list import ReservationListMap

class ReservationList(ReservationListMap, BaseData):

    @property
    def items(self):
        return self.reservation_id.items

    def __init__(self):
        self.reservation_id = BaseResourceSimpleList(ReservationData)

    def add(self, id=None):
        new_reservation = self.reservation_id.add()
        if (new_reservation is not None):
            new_reservation.reservation_id = id
        return new_reservation