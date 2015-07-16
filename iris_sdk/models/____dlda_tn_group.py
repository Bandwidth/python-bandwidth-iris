#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.dlda_tn_group import DldaTnGroupData

XPATH_DLDA_TN_GROUP = "/{}"

class DldaTnGroup(BaseResource, DldaTnGroupData):

    _xpath = XPATH_DLDA_TN_GROUP

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        DldaTnGroupData.__init__(self)