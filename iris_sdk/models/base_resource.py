#!/usr/bin/env python

from xml.etree import ElementTree

from iris_sdk.utils.strings import Converter

BASE_PROP_CLIENT = "client"
BASE_PROP_XPATH = "xpath"

class BaseData(object):

    def clear(self):
        for prop in dir(self):
            property = getattr(self, prop)
            if (prop.startswith("_")) or (prop == BASE_PROP_CLIENT) or \
                    (prop == BASE_PROP_XPATH) or (callable(property)):
                continue
            cleared = False
            _class = property.__class__
            if (_class == BaseData) or (_class == BaseResourceList):
                property.clear()
                cleared = True
            else:
                for classtype in property.__class__.__bases__:
                    if (classtype==BaseData) or (classtype==BaseResourceList)\
                            or (classtype==BaseResource):
                        property.clear()
                        cleared = True
                        break
            if (not cleared):
                setattr(self, prop, None)

class BaseResourceList(object):

    """List of instances of "class_type" passed to constructor"""

    def __init__(self, class_type, parent=None):
        self._items = []
        self._class_type = class_type
        self._parent = parent

    @property
    def class_type(self):
        return self._class_type

    @property
    def items(self):
        return self._items

    @property
    def parent(self):
        return self._parent

    def clear(self):
        del self.items[:]

class BaseResourceSimpleList(BaseResourceList):
    pass

class BaseResource(BaseData):

    """REST resource"""

    _parent = None
    _xpath = ""
    _id = None

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def client(self):
        return self._client
    @client.setter
    def client(self, client):
        self._client = client

    @property
    def xpath(self):
        return self._xpath

    def __init__(self, parent=None, client=None):
        self._converter = Converter()
        self._parent = parent
        self._client = client
        if (client is None):
            self._client = parent.client

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
                print(tag)
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
                    # Set parents for REST resources.
                    has_parent = False
                    for class_type in property.class_type.__bases__:
                        if class_type == BaseResource:
                            has_parent = True
                            break
                    _class = property.class_type
                    if (has_parent):
                        item = property.class_type(property.parent)
                    else:
                        item = property.class_type()
                    property.items.append(item)
                    _inst = property.items[-1]
                # Instance's class mirrors the element's structure.
                self._parse_xml(el, _inst)

    def get(self, id=None, params=None):
        return self.get_data(id, params)

    def get_data(self, id=None, params=None):

        self.clear()

        self.id = (id or "")

        xpath = self.get_xpath()

        response_str = self._client.get(xpath, params)
        root = ElementTree.fromstring(response_str)
        self._parse_xml(root)

        return self

    def get_status(self, id=None, params=None):
        xpath = self._get_xpath(id)
        return self._client.get(xpath, params, True)

    def get_xpath(self):
        parent_path = ""
        if (self._parent is not None):
            parent_path = self._parent.get_xpath()
        xpath = parent_path + self._xpath
        return xpath.format(self.id)