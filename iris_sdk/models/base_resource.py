#!/usr/bin/env python

from xml.etree import ElementTree

from iris_sdk.utils.strings import Converter

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
    def _parse_xml(self, element, instance=None):

        """
        Parses XML elements into existing objects, e.g.:

        garply = some_class()
        garply.foo = some_other_class()
        garply.foo.bar_baz = None

        <Foo><BarBaz>Qux</Bar></Foo> -> garply.foo.bar_baz equals "qux".

        Converts CamelCase names to lowercase underscore ones.
        """

        # If instance is None, the tag name to search for in XML data equals
        # class name.

        inst = (self if instance is None else instance)
        class_name = inst.__class__.__name__

        node_name = None
        if hasattr(inst, "_node_name"):
            node_name = inst._node_name

        # Recursive call: instance's class represents the element's structure.
        if (instance is not None):
            search_name = element.tag
        else:
            search_name = (class_name if node_name is None else node_name)

        # The provided element is actually the one we're searching for.
        if (element.tag == search_name):
            element_children = element.getchildren()
        else:
            element_children = element.findall(search_name)

        for el in element_children:

            tag = self._converter.to_underscore(el.tag)

            property = None
            if (not hasattr(inst, tag)):
                # Not the base class.
                if (instance is not None):
                    continue
            else:
                property = getattr(inst, tag)

            if (len(el.getchildren()) == 0):
                setattr(inst, tag, el.text)
            else:
                _inst = property
                # Simple list.
                if (isinstance(property, BaseResourceSimpleList)):
                    for child in el.getchildren():
                        child_tag = self._converter.to_underscore(child.tag)
                        item = property.class_type()
                        if (hasattr(item, child_tag)):
                            setattr(item, child_tag, child.text)
                            property.items.append(item)
                    continue
                # List of instances - add an item and parse recursively.
                if (isinstance(property, BaseResourceList)):
                    property.items.append(property.class_type())
                    _inst = property.items[-1]
                # Instance's class mirrors the element's structure.
                self._parse_xml(el, _inst)

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

class BaseResourceList(object):

    """List of instances of "class_type" passed to constructor"""

    def __init__(self, class_type):
        self._items = []
        self._class_type = class_type

    @property
    def class_type(self):
        return self._class_type

    @property
    def items(self):
        return self._items

    def clear(self):
        del self.items[:]

class BaseResourceSimpleList(BaseResourceList):
    pass