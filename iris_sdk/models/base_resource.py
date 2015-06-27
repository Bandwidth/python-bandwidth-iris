#!/usr/bin/env python

from iris_sdk.utils.strings import Converter
from xml.etree import ElementTree

DATA_LIST_NAME = "items"

class BaseResource(object):

    """REST resource"""

    _xpath = ""

    def __init__(self, client=None, xpath=None):

        self._client = client
        if (xpath is not None):
            self._xpath = xpath + self._xpath
        self._converter = Converter()

    def _get_xpath(self, id=None):
        return self._xpath.format(
            self._client.config.account_id, (id if id is not None else None))

    # TODO: back - object to xml
    def _parse_xml(self, element=None, instance=None, classname=None):

        """
        Parses XML elements into existing objects, e.g.:

        garply = foo()
        <Foo><BarBaz>Qux</Bar></Foo> -> garply.bar_baz equals "qux".

        Converts lowercase names to CamelCase.
        """

        inst = (self if instance is None else instance)
        base_class = inst.__class__

        # Search elements by "classname" instead of the name of the class
        if (classname is None):
            class_name = self._converter.to_camelcase(base_class.__name__)
        else:
            class_name = classname

        # If a class has different resource types returned in one xml
        # under the root elements.
        if (element.tag == class_name):
            element_children = element.getchildren()
        else:
            element_children = element.findall(class_name)

        for el in element_children:
            # If the element we're searching for doesn't have any children.
            if (len(el.getchildren()) == 0):
                tags = []
                tags.append(el)
            else:
                tags = el.getchildren()
            check_tag = self._converter.to_underscore(el.tag)

            if (hasattr(base_class, check_tag)):
                property = getattr(inst, check_tag)
            else:
                property = None
            # A list of elements - use append()
            is_list = (property is not None) and (isinstance(property, list))
            for prop in tags:
                tag = self._converter.to_underscore(prop.tag)
                if (not hasattr(base_class, tag)) and (not is_list):
                    continue
                if (len(prop.getchildren()) == 0):
                    if (is_list):
                        property.append(prop.text)
                    else:
                        setattr(inst, tag, prop.text)
                else:
                   _class = getattr(inst, tag)
                   self._parse_xml(el, _class)

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def xpath(self):
        return self._xpath

    def get_data(self, id=None, params=None, node_name=None):

        xpath = self._get_xpath(id)

        response_str = self._client.get(xpath, params)
        root = ElementTree.fromstring(response_str)
        self._parse_xml(element=root, classname=node_name)

        return self

    def get_status(self, id=None, params=None, node_name=None):
        xpath = self._get_xpath(id)
        return self._client.get(xpath, params, True)