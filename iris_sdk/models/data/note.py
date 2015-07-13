#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.note import NoteMap

class NoteData(NoteMap, BaseData):
    pass