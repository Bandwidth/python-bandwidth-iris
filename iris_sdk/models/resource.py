#!/usr/bin/env python

from xml.etree import ElementTree

class BaseResource():

    """REST resource"""

    def __init__(self, client=None):

        self._client = client
        self._id = None
        self._xpath = None

    # TODO: back, underscore<->CamelCase
    def _parse_xml(self, element=None, class_type=None):
        base_class = (self.__class__ if class_type is None else class_type)
        el = element.findall(base_class.__name__)
        element_children = el.getchildren()
        for prop in element_children:
            if hasattr(base_class, prop.tag):
                if (len(prop.getchildren()) == 0):
                    setattr(base_class, prop.tag, prop.text)
                else:
                   _class = getattr(base_class, prop.tag)
                   setattr(base_class, prop.tag, _class())
                   self._parse_xml(prop, _class)

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def id(self):
        return self._id

    def get(id, params=None):
        response_str = self._client.get(id, self._xpath.format(id), params)
        root = ElementTree.fromstring(response_str)
        self._parse_xml(root)


class BaseList(BaseResource):

    """A collection of resources"""

    pass