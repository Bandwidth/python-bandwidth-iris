#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class ImportTnCheckerResponseMap(BaseMap):

    import_tn_checker_payload = None
    telephone_numbers = None
    import_tn_errors = None
