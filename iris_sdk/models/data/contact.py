#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.contact import ContactMap

class Contact(ContactMap, BaseData):
    pass