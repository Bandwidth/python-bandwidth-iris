#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.note import Note
from iris_sdk.models.maps.notes import NotesMap

class NotesData(NotesMap, BaseData):

    def __init__(self, parent=None):
        self.note = BaseResourceList(Note, parent)