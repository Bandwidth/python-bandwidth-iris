#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.telephone_number_list import TelephoneNumberList
from iris_sdk.models.maps.ord.existing_search_order import \
    ExistingSearchOrderMap
from iris_sdk.models.data.reservation_list import ReservationList

class ExistingSearchOrder(ExistingSearchOrderMap, BaseData):

    def __init__(self):
        self.reservation_id_list = ReservationList()
        self.telephone_number_list = TelephoneNumberList()