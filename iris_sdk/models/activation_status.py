#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.maps.activation_status import ActivationStatusMap

XPATH_ACTIVATION_STATUS = "/activationStatus"

class ActivationStatus(BaseResource, ActivationStatusMap):

    """Local number portability order activation status"""

    _xpath = XPATH_ACTIVATION_STATUS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        self._id = 1

    def get(self):
        return self._get_data()

    def save(self):
        self.id = 1
        self._save()