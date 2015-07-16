#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.line_options import LineOptionsData

XPATH_LINE_OPTIONS = "/{}"

class LineOptions(BaseResource, LineOptionsData):

    """ Establish Calling Name Display settings for a collection of TNs at a time """

    _xpath = XPATH_LINE_OPTIONS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LineOptionsData.__init__(self)