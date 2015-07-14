#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.portins import PortInsData
from iris_sdk.models.portin import PortIn

XML_NAME_PORTINS = "LNPResponseWrapper"
XPATH_PORTINS = "/portins"

class PortIns(BaseResource, PortInsData):

    """Local number portability orders for account"""

    _node_name = XML_NAME_PORTINS
    _xpath = XPATH_PORTINS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        PortInsData.__init__(self, self)

    def add(self):
        return PortIn(self)

    def get(self, id, params):
        return self.add().get(id, params=params)

    def list(self, params):
        return self._get_data(params=params).lnp_port_info_for_given_status

    def create(self, initial_data, save=True):
        portin = self.add()
        portin.set_from_dict(initial_data)
        if save:
            portin.save()
        return portin