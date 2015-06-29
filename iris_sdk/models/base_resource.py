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
    def _parse_xml(self, element=None, instance=None):

        """
        Parses XML elements into existing objects, e.g.:

        garply = foo()
        <Foo><BarBaz>Qux</Bar></Foo> -> garply.bar_baz equals "qux".

        Converts lowercase names to CamelCase.
        """

        inst = (self if instance is None else instance)
        base_class = inst.__class__

        node_name = None
        if hasattr(inst, "_node_name"):
            node_name = inst._node_name

        search_name = (inst.__class__.__name__ if node_name is None else \
            inst._node_name)

        # Searching for the root.
        if (element.tag == search_name):
            element_children = element
        else:
            element_children = element.findall(search_name)

        for el in element_children:

            tag = self._converter.to_underscore(el.tag)

            if (hasattr(base_class, tag)):
                try:
                    property = getattr(inst, tag)
                except:
                    #print(tag)
                    break
            else:
                property = None

            if (property is None) and (search_name != base_class.__name__) and\
                    (node_name is None):
                continue

            if (len(el.getchildren()) == 0):
                try:
                    setattr(inst, tag, el.text)
                except:
                    print(inst)
                    print(tag)
                    #break
            else:
                _inst = property
                if (isinstance(property, BaseResourceList)):
                    class_type = property.items[0].__class__
                    property.items.append(class_type())
                    _inst = property.items[-1]
                elif (isinstance(property, list)):
                    for item in el.getchildren():
                        property.append(item.text)
                self._parse_xml(el, _inst)

    def _prepare_list(self, items):
        del items[0]

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def xpath(self):
        return self._xpath

    def get_data(self, id=None, params=None):
        xpath = self._get_xpath(id)

        response_str = self._client.get(xpath, params)
        root = ElementTree.fromstring(response_str)
        self._parse_xml(root)

        return self

    def get_status(self, id=None, params=None):
        xpath = self._get_xpath(id)
        return self._client.get(xpath, params, True)

class BaseResourceList(list):

    """REST list of BaseResource items"""

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items