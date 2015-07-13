#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.maps.tn_attributes import TnAttributesMap

class TnAttributes(TnAttributesMap, BaseData):

    @property
    def items(self):
        return self.tn_attribute.items

    def __init__(self, parent=None):
        self.tn_attribute = BaseResourceSimpleList()