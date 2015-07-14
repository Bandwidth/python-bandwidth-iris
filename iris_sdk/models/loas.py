#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.loas import LoasData

XML_NAME_LOAS = "FileListResponse"
XPATH_LOAS_FILENAME = "/{}"
XPATH_LOAS = "/loas"

class Loas(BaseResource, LoasData):

    """Local number portability order LOAs"""

    _node_name = XML_NAME_LOAS
    _xpath = XPATH_LOAS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LoasData.__init__(self)

    def delete(self, id):
        pass

    def get(self):
        pass

    def list(self, params=None):
        return self._get_data(params)

    def add(self, filename, headers):
        return self._send_file("", filename, headers)

    def update(self, id, filename, headers):
        return self._send_file(XPATH_LOAS_FILENAME.format(id),
            filename, headers, id)

    def get_metadata(self, id):
        pass

    def set_metadata(self, id, metadata):
        pass

    def delete_metadata(self, id):
        pass