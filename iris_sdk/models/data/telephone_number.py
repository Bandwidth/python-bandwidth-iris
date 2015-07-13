#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.telephone_number import TelephoneNumberMap

class TelephoneNumberData(TelephoneNumberMap, BaseData):

    @property
    def last_modified_date(self):
        return self.last_modified
    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        self.last_modified = last_modified_date