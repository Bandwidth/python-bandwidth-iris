#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.import_tn_checker_list import TelephoneNumbers
from iris_sdk.models.maps.import_tn_checker import ImportTnCheckerMap

class ImportTnCheckerData(ImportTnCheckerMap, BaseData):

    def __init__(self):
        self.telephone_numbers = TelephoneNumbers()
