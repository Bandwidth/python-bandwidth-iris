#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.dldas import DldasMap
from iris_sdk.models.dlda import Dlda

class DldasData(DldasMap, BaseData):

    def __init__(self, parent=None):
        self.order_id_user_id_date = BaseResourceList(Dlda, parent)