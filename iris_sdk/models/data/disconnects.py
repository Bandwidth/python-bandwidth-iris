#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.links import Links
from iris_sdk.models.maps.disconnects import DisconnectsMap
from iris_sdk.models.disconnect import Disconnect

class DisconnectsData(DisconnectsMap, BaseData):

    def __init__(self, parent=None):
        self.links = Links()
        self.order_id_user_id_date = BaseResourceList(Disconnect, parent)