#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.npanxx import NpanxxMap

class Npanxx(NpanxxMap, BaseData):

    @property
    def npa_nxx_x(self):
        return self.npanxx
    @npa_nxx_x.setter
    def npa_nxx_x(self, npa_nxx_x):
        self.npanxx = npa_nxx_x