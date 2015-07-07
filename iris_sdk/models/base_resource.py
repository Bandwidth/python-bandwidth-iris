#!/usr/bin/env python

from inspect import getmro
from io import BytesIO
from xml.etree.ElementTree import Element, ElementTree, fromstring, SubElement

from iris_sdk.models.maps.base_map import BaseMap
from iris_sdk.utils.strings import Converter

BASE_ID_SKIP = -77777;
BASE_MAP_SUFFIX = "Map"
BASE_PROP_CLIENT = "client"
BASE_PROP_ITEMS = "items"
BASE_PROP_NODE = "_node_name"
BASE_PROP_XPATH = "xpath"

class BaseData(object):

    """Base class for everything"""

    def clear(self):

        """Flushes the data"""

        for prop in dir(self):

            property = getattr(self, prop)

            # Might be needed
            if (prop.startswith("_")) or (prop == BASE_PROP_CLIENT) or \
                    (prop == BASE_PROP_XPATH) or (prop == BASE_PROP_ITEMS) or\
                    (callable(property)):
                continue

            cleared = False
            _class = property.__class__

            # Everything is either a BaseData, a BaseResourceList or a
            # BaseResource descendant (which itself inherits from BaseData).
            if (_class == BaseData) or (_class == BaseResourceList):
                property.clear()
                cleared = True
            else:
                for classtype in getmro(property.__class__):
                    if (classtype==BaseData) or (classtype==BaseResourceList)\
                            or (classtype==BaseResource):
                        property.clear()
                        cleared = True
                        break

            # Built-in types
            if (not cleared):
                setattr(self, prop, None)

class BaseResourceList(object):

    """
    List of instances of "class_type" passed to constructor.
    "parent" used to link BaseResource instances and pass their "client"
    properties.
    """

    @property
    def class_type(self):
        return self._class_type

    @property
    def items(self):
        return self._items

    @property
    def parent(self):
        return self._parent

    def __init__(self, class_type, parent=None):
        self._items = []
        self._class_type = class_type
        self._parent = parent

    def add(self):
        if (self.parent is not None):
            item = self.class_type(self.parent)
        else:
            item = self.class_type()
        self.items.append(item)
        return item

    def clear(self):
        del self.items[:]

class BaseResourceSimpleList(BaseResourceList):

    """
    Same as BaseResourceList, but used to store instances with a single
    property.
    Just for convenience in XML parsing.
    """

    pass

class BaseResource(BaseData):

    """
    REST resource.
    "client" does http requests,
    "xpath" returns the REST resource's relative path.
    """

    _id = None
    _parent = None
    _node_name = None
    _xpath = ""

    @property
    def client(self):
        return self._client
    @client.setter
    def client(self, client):
        self._client = client

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def xpath(self):
        return self._xpath

    def __init__(self, parent=None, client=None):
        self._converter = Converter()
        self._parent = parent
        self._client = client
        if (client is None) and (parent is not None):
            self._client = parent.client

    def _from_xml(self, element, instance=None):

        """
        Parses XML elements into existing objects, e.g.:

        garply = some_class(),
        garply._node_name = "Foo"
        garply.bar_baz = some_other_class()
        garply.bar_baz.qux = None

        <Foo>
            <BarBaz>
                <Qux>Corge</Qux>
            </BarBaz>
        </Foo>

        garply.bar_baz.qux equals "Corge".

        Converts CamelCase names to lowercase underscore ones.
        """

        # If instance is None, the tag name to search for in XML data equals
        # class name.

        inst = (instance or self)
        class_name = inst.__class__.__name__

        node_name = None
        if hasattr(inst, BASE_PROP_NODE):
            node_name = inst._node_name

        # Recursive call: instance's class represents the element's structure
        if (instance is not None):
            search_name = element.tag
        else:
            search_name = (node_name or class_name)

        # The provided element is actually the one we're searching for
        if (element.tag == search_name):
            element_children = element.getchildren()
        else:
            element_children = element.findall(search_name)

        for el in element_children:

            tag = self._converter.to_underscore(el.tag)

            property = None
            if (not hasattr(inst, tag)):
                # Not the base class
                if (instance is not None):
                    continue
            else:
                property = getattr(inst, tag)

            if (len(el.getchildren()) == 0):
                if (el.text is not None):
                    setattr(inst, tag, el.text)
            else:
                _inst = property
                # Simple list - multiple "<tag></tag>" lines
                if (isinstance(property, BaseResourceSimpleList)):
                    for child in el.getchildren():
                        child_tag = self._converter.to_underscore(child.tag)
                        item = property.class_type()
                        if (hasattr(item, child_tag)):
                            setattr(item, child_tag, child.text)
                            property.items.append(item)
                    continue
                # List of instances - add an item and parse recursively
                if (isinstance(property, BaseResourceList)):
                    # Set parents for REST resources
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
                # Instance's class mirrors the element's structure
                self._from_xml(el, _inst)

    def _get_data(self, id=None, params=None, xpath=None):

        new_id = (id if id is not None else self.id)

        if (xpath is None):
            self.clear()

        self.id = new_id

        _xpath = self.get_xpath() + (xpath or "")

        response_str = self._client.get(_xpath, params)
        root = fromstring(response_str)
        self._from_xml(root)

        return self

    def _post_data(self, xpath, data):
        return self._client.post(section=xpath, data=data)

    def _put_data(self, xpath, data):
        return self._client.put(section=xpath, data=data)

    def _to_xml(self, element=None, instance=None):

        """
        The opposite of "_from_xml".
        Lowercase underscore names are converted to CamelCase.
        """

        inst = (instance or self)

        # Renaming the root
        node_name = inst.__class__.__name__
        if hasattr(inst, BASE_PROP_NODE):
            if (inst._node_name is not None):
                node_name = inst._node_name

        elem = (Element(node_name) if element is None else element)

        map = None

        # "Map" is a base class that sets the correspondence between XML
        # elements and class properties, i.e. what's not in this class doesn't
        # get written to the file.

        for classtype in getmro(inst.__class__):
            if (classtype.__name__.endswith(BASE_MAP_SUFFIX) and \
                    classtype.__name__ != BaseMap.__name__):
                map = classtype
                break

        if (map is None):
            return elem

        for prop in dir(map):

            property = getattr(inst, prop)

            if (prop.startswith("_")) or (callable(property)) or \
                    (property is None):
                continue

            # Lists

            if (isinstance(property, BaseResourceList)):
                for item in property.items:
                    el = SubElement(elem, self._converter.to_camelcase(prop))
                    self._to_xml(el, item)
                continue

            if (isinstance(property, list)) and (prop != BASE_PROP_ITEMS):
                for item in property:
                    el = SubElement(elem, self._converter.to_camelcase(prop))
                    el.text = str(item)
                continue

            # Everything else

            el = SubElement(elem, self._converter.to_camelcase(prop))

            if (isinstance(property, BaseMap)):
                self._to_xml(el, property)
            else:
                el.text = property

        return elem

    def delete(self):
        return self._client.delete(self.get_xpath())

    def get(self, id=None, params=None):
        return self._get_data(id, params)

    def get_status(self, id=None, params=None):
        xpath = self._get_xpath(id)
        return self._client.get(xpath, params, True)

    def get_xpath(self):
        parent_path = ""
        if (self._parent is not None):
            parent_path = self._parent.get_xpath()
        xpath = parent_path + self._xpath
        return xpath.format(self.id)

    def save(self):

        root = ElementTree(self._to_xml())
        data_io = BytesIO()
        root.write(data_io, encoding="UTF-8", xml_declaration=True)
        data = data_io.getvalue()

        if (self.id is not None) and (self.id != BASE_ID_SKIP):
            return self._put_data(self.get_xpath(), data)
        elif (self.id == BASE_ID_SKIP):
            self._post_data(self.get_xpath(), data)
            return True
        else:
            self.id=self._post_data(self._parent.get_xpath(), data)
            return True