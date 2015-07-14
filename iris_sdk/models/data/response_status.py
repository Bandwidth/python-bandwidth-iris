#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.response_status import ResponseStatusMap

class ResponseStatus(ResponseStatusMap, BaseData):
    pass