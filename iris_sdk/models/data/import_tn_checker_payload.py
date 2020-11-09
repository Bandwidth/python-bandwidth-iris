#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.data.import_tn_checker_list import TelephoneNumbers

class ImportTnCheckerResponse(TelephoneNumbers, BaseData):

    @property
    def items(self):
        return self.telephone_numbers.items

    def __init__(self):
        self.telephone_numbers = TelephoneNumbers()
