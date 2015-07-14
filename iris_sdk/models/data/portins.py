#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.data.links import Links
from iris_sdk.models.data.portin import PortIn
from iris_sdk.models.maps.portins import PortInsMap

class PortInsData(PortInsMap, BaseData):

    def __init__(self, parent=None):
        self.links = Links()
        self.lnp_port_info_for_given_status = BaseResourceList(PortIn, parent)