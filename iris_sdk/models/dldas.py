#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.dldas import DldasData
from iris_sdk.models.dlda import Dlda

XML_NAME_DLDAS = "ListOrderIdUserIdDate"
XPATH_DLDAS = "/dldas"

class Dldas(BaseResource, DldasData):

    """ DLDA orders """

    _node_name = XML_NAME_DLDAS
    _xpath = XPATH_DLDAS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        DldasData.__init__(self, self)

    def create(self, data=None, save=True):
        dlda = Dlda(self).set_from_dict(data)
        if save and (data is not None):
            dlda.save()
        return dlda

    def get(self, id, params=None):
        return Dlda(self).get(id, params=params)

    def list(self, params=None):
        return self._get_data(params=params).order_id_user_id_date