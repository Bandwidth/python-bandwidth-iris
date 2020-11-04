#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.import_tn_checker_payload import ImportTnCheckerResponse
from iris_sdk.models.maps.import_tn_checker_response import ImportTnCheckerResponseMap

class ImportTnCheckerResponseData(ImportTnCheckerResponseMap, BaseData):

    def __init__(self):
        self.import_tn_checker_payload = ImportTnCheckerResponse()
