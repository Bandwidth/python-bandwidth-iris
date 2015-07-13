#!/usr/bin/env python

from future.standard_library import install_aliases
install_aliases()

from urllib.parse import parse_qs, urlparse

from iris_sdk.include.xml_consts import XML_PARAM_PAGE
from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.links import LinksMap

LINK_PREFIX = "<"
LINK_SUFFIX = ">"

class Links(LinksMap, BaseData):

    _first = None
    _next = None

    @property
    def first(self):
        return self._first
    @first.setter
    def first(self, first):
        if (first is None):
            self._first = None
            return
        url =(first or "").partition(LINK_PREFIX)[2].partition(LINK_SUFFIX)[0]
        params = parse_qs(urlparse(url).query)
        self._first = params[XML_PARAM_PAGE]

    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, next):
        if (next is None):
            self._next = None
            return
        url = (next or "").partition(LINK_PREFIX)[2].partition(LINK_SUFFIX)[0]
        params = parse_qs(urlparse(url).query)
        self._next = params[XML_PARAM_PAGE]