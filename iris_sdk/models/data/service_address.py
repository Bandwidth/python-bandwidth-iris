#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.address import AddressMap

class ServiceAddress(AddressMap, BaseData):
    pass