#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.tn_status import TnStatus
from iris_sdk.models.maps.tn_history import TnHistoryMap

class TnHistoryData(TnHistoryMap):

    def __init__(self):
        self.telephone_number_status = BaseResourceList(TnStatus)