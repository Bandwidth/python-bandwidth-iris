#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.feature_dlda import FeatureDlda
from iris_sdk.models.data.feature_lidb import FeatureLidb
from iris_sdk.models.maps.features import FeaturesMap

class Features(FeaturesMap, BaseData):

    def __init__(self):
        self.dlda = FeatureDlda()
        self.lidb = FeatureLidb()