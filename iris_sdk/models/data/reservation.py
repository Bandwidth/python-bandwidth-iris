#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.reservation import ReservationMap

class Reservation(ReservationMap, BaseData):

    @property
    def account(self):
        return self.account_id
    @account.setter
    def account(self, account):
        self.account_id = account

    @property
    def reservation_id(self):
        return self.id
    @reservation_id.setter
    def reservation_id(self, reservation_id):
        self.id = reservation_id