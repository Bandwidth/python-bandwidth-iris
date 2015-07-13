#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.notes import NotesData
from iris_sdk.models.note import Note

XPATH_NOTES = "/notes"

class Notes(BaseResource, NotesData):

    """Order notes"""

    _save_post = True
    _xpath = XPATH_NOTES
    _xpath_save = _xpath

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        NotesData.__init__(self, self)

    def add(self):
        return Note(self)

    def list(self):
        return self._get_data().note