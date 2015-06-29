#!/usr/bin/env python

from future.standard_library import install_aliases
install_aliases()

from urllib.parse import parse_qs, urlparse

LINK_PREFIX = "<"
LINK_SUFFIX = ">"

class LinksData(object):

    @property
    def first(self):
        return self._first
    @first.setter
    def first(self, first):
        url =(first or "").partition(LINK_PREFIX)[2].partition(LINK_SUFFIX)[0]
        params = parse_qs(urlparse(url).query)
        self._first = params["page"]

    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, next):
        url =(next or "").partition(LINK_PREFIX)[2].partition(LINK_SUFFIX)[0]
        params = parse_qs(urlparse(url).query)
        self._next = params["page"]

class Links(LinksData):

    def __init__(self):
        self.clear()

    def clear(self):
        self._first = None
        self._next = None