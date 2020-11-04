#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class ImportTnCheckerPayloadMap(BaseMap):

    telephone_numbers = None
    import_tn_errors = None
