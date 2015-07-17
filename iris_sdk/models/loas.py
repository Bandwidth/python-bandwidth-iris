#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.include.xml_consts import XML_PARAM_METADATA, XML_TRUE
from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.loas import LoasData
from iris_sdk.models.file_meta_data import FileMetaData

XML_NAME_LOAS = "FileListResponse"
XPATH_LOAS_FILENAME = "/{}"
XPATH_LOAS = "/loas"

class Loas(BaseResource, LoasData):

    """Local number portability order LOAs"""

    _node_name = XML_NAME_LOAS
    _xpath = XPATH_LOAS

    @property
    def metadata(self):
        return self._metadata

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LoasData.__init__(self)
        self._metadata = FileMetaData(self, client)

    def create(self, filename, headers):
        return self._send_file("", filename, headers)

    def delete(self, id):
        return self._delete_file(XPATH_LOAS_FILENAME, id)

    def get(self, id):
        return self._get_file(XPATH_LOAS_FILENAME, id)

    def list(self, params=None):
        self._get_data(params=params)
        if params.get(XML_PARAM_METADATA.lower(), "") == XML_TRUE:
            return self.file_data
        else:
            return self.file_names

    def update(self, id, filename, headers):
        return self._send_file(XPATH_LOAS_FILENAME, filename, headers, id)