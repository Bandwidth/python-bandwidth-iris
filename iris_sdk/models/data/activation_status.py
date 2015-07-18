#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.telephone_number_list import TelephoneNumberList
from iris_sdk.models.maps.activation_status import ActivationStatusMap

class ActivationStatusData(ActivationStatusMap, BaseData):

    def __init__(self):
        self.activated_telephone_numbers_list = TelephoneNumberList()
        self.not_yet_activated_telephone_numbers_list = TelephoneNumberList()