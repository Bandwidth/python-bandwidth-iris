#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.dlda import Dlda
from iris_sdk.models.data.lidb import Lidb
from iris_sdk.models.maps.features import FeaturesMap

class Features(FeaturesMap, BaseData):

    def __init__(self):
        self.dlda = Dlda()
        self.lidb = Lidb()