#!/usr/bin/env python

from inspect import getmro
from io import BytesIO
from xml.etree.ElementTree import Element, ElementTree, fromstring, SubElement

from iris_sdk.models.maps.base_map import BaseMap
from iris_sdk.utils.rest import HTTP_OK
from iris_sdk.utils.strings import Converter

BASE_MAP_SUFFIX = "Map"
BASE_PROP_CLIENT = "client"
BASE_PROP_ITEMS = "items"
BASE_PROP_NODE = "_node_name"
BASE_PROP_NODE_SAVE = "_node_name_save"
BASE_PROP_XPATH = "xpath"
BASE_PROP_XPATH_SEPARATOR = "{"
HEADER_LOCATION = "location"

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
            if (_class == BaseData) or (_class == BaseResourceList) or \
                    (_class == BaseResourceSimpleList):
                property.clear()
                cleared = True
            else:
                for classtype in getmro(property.__class__):
                    if (classtype==BaseData) or (classtype==BaseResourceList)\
                            or (classtype==BaseResource) or \
                            (classtype==BaseResourceSimpleList):
                        property.clear()
                        cleared = True
                        break

            # Built-in types
            if not cleared:
                setattr(self, prop, None)

    def set_from_dict(self, initial_data=None):
        if initial_data is not None and isinstance(initial_data, dict):
            self.clear()
            for key in initial_data:
                if hasattr(self, key):
                    if isinstance(initial_data[key], basestring):
                        setattr(self, key, initial_data[key])
                    else:
                        attr = getattr(self, key)
                        if isinstance(initial_data[key], dict):
                            if attr is None:
                                """ attr should be already not None by the
                                moment of calling set_from_dict,
                                but just in case: """
                                attr = BaseResource()
                                attr.set_from_dict(initial_data[key])
                                setattr(self, key, attr)
                            elif isinstance(attr, BaseData):
                                attr.set_from_dict(initial_data[key])
                        elif isinstance(initial_data[key], list):
                            if attr is None:
                                """ attr should be already not None by the
                                moment of calling set_from_dict,
                                but just in case: """
                                setattr(self, key,
                                    BaseResourceList(BaseResource))
                                attr = getattr(self, key)
                            if isinstance(attr, BaseResourceSimpleList):
                                attr.clear()
                                for list_item in initial_data[key]:
                                    attr.add(list_item)
                                setattr(self, key, attr)
        return self

class BaseResourceSimpleList(object):

    """
    Used to store simple values.
    """

    @property
    def items(self):
        return self._items

    def __init__(self):
        self._items = []

    def add(self, value):
        self.items.append(value)
        return self.items[-1]

    def clear(self):
        del self.items[:]

class BaseResourceList(BaseResourceSimpleList):

    """
    List of instances of "class_type" passed to constructor.
    "parent" used to link BaseResource instances and pass their "client"
    properties.
    """

    @property
    def class_type(self):
        return self._class_type

    @property
    def parent(self):
        return self._parent

    def __init__(self, class_type, parent=None):
        BaseResourceSimpleList.__init__(self)
        self._class_type = class_type
        self._parent = parent

    def add(self, initial_data=None):
        if self.parent is not None:
            item = self.class_type(self.parent)
        else:
            item = self.class_type()
        item.set_from_dict(initial_data)
        self.items.append(item)
        return item

class BaseResource(BaseData):

    """
    REST resource.

    "_node_name" - corresponding XML element name,
    "_save_post" - uses POST if True, PUT - otherwise,
    "_xpath_save" - if set, uses this for saving,
    "client" does http requests,
    "xpath" returns the REST resource's relative path.
    """

    _id = None
    _parent = None
    _node_name = None
    _node_name_save = None
    _save_post = False
    _xpath = ""
    _xpath_save = None

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

    def _element_from_string(self, str):
        return fromstring(str)

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
        if instance is not None:
            search_name = element.tag
        else:
            search_name = (node_name or class_name)

        # The provided element is actually the one we're searching for
        if element.tag == search_name:
            element_children = element.getchildren()
        else:
            element_children = element.findall(search_name)

        for el in element_children:

            tag = self._converter.to_underscore(el.tag)

            property = None
            if not hasattr(inst, tag):
                # Not the base class
                if instance is not None:
                    continue
            else:
                property = getattr(inst, tag)

            if len(el.getchildren()) == 0:
                if el.text is not None:
                    # Simple list - multiple "<tag></tag>" lines
                    if isinstance(property, BaseResourceSimpleList):
                        property.items.append(el.text)
                    else:
                        setattr(inst, tag, el.text)
                continue

            _inst = property

            # List of instances - add an item and parse recursively
            if isinstance(property, BaseResourceList):
                # Set parents for REST resources
                has_parent = False
                for class_type in property.class_type.__bases__:
                    if class_type == BaseResource:
                        has_parent = True
                        break
                self._class = property.class_type
                if has_parent:
                    item = property.class_type(property.parent)
                else:
                    item = property.class_type()
                property.items.append(item)
                _inst = property.items[-1]

            # Instance's class mirrors the element's structure
            self._from_xml(el, _inst)

    def _get(self, id=None, params=None):
        new_id = (id or self.id)
        self.clear()
        self.id = new_id
        xpath = self.get_xpath()
        if (self.id is None) and (BASE_PROP_XPATH_SEPARATOR in xpath):
            raise ValueError("No id specified")
        return self._client.get(self.get_xpath(), params)

    def _get_data(self, id=None, params=None):
        content = self._get(id, params).content.decode(encoding="UTF-8")
        if content:
            root = self._element_from_string(content)
            self._from_xml(root)
        return self

    def _post_data(self, response_instance=None, params=None):
        content = self._save(return_content=True, params=params)
        if content:
            root = self._element_from_string(content)
            if response_instance is not None:
                response_instance._from_xml(root)
                return response_instance
            else:
                self._from_xml(root)
        return self

    def _get_status(self, id=None, params=None):
        return self._get(id, params).status

    def _post(self, xpath, data, params):
        return self._client.post(section=xpath, params=params, data=data)

    def _send_file(self, xpath, filename, headers, id=None):

        request = self._client.post
        if id is not None:
            request = self._client.put

        with open(filename, 'rb') as file_data:
            response = request(section=self.get_xpath(True) + xpath,
                        data=file_data, headers=headers)

        location = None
        if HEADER_LOCATION in response.headers:
            location = response.headers[HEADER_LOCATION]

        if location is not None:
            return location[location.rfind("/")+1:]
        else:
            return response.status_code == HTTP_OK

    def _put(self, xpath, data):
        return self._client.put(section=xpath, data=data)

    def _save(self, return_content=False, params=None):

        data = self._serialize()

        if (self.id is not None) and (not self._save_post):
            response = self._put(self.get_xpath(True), data)
            if return_content:
                return response.content.decode(encoding="UTF-8")
            else:
                return response.status_code == HTTP_OK

        resource = (self if self._save_post else self._parent)
        path = resource.get_xpath(True)

        response = self._post(path, data, params)

        if return_content:
            return response.content.decode(encoding="UTF-8")

        location = response.headers[HEADER_LOCATION]
        res = ""
        if location is not None:
            pos = location.rfind("/")
            res = location[pos+1:]

        self.id = (res if res else self.id)
        return True

    def _serialize(self):
        root = ElementTree(self._to_xml())
        data_io = BytesIO()
        root.write(data_io, encoding="UTF-8", xml_declaration=True)
        return data_io.getvalue()

    def _to_xml(self, element=None, instance=None):

        """
        The opposite of "_from_xml".
        Lowercase underscore names are converted to CamelCase.
        """

        inst = (instance or self)

        # Renaming the root
        node_name = inst.__class__.__name__

        if hasattr(inst, BASE_PROP_NODE):
            if inst._node_name is not None:
                node_name = inst._node_name

        if hasattr(inst, BASE_PROP_NODE_SAVE):
            if inst._node_name_save is not None:
                node_name = inst._node_name_save

        elem = (Element(node_name) if element is None else element)

        map = None

        # "Map" is a base class that sets the correspondence between XML
        # elements and class properties, i.e. what's not in this class doesn't
        # get written to the file.

        for classtype in getmro(inst.__class__):
            if (classtype.__name__.endswith(BASE_MAP_SUFFIX) and
                    classtype.__name__ != BaseMap.__name__):
                map = classtype
                break

        if map is None:
            return elem

        for prop in dir(map):

            property = getattr(inst, prop)

            if (prop.startswith("_") or
                callable(property) or
                property is None):
                continue

            # Lists

            if isinstance(property, BaseResourceList):
                for item in property.items:
                    el = SubElement(elem, self._converter.to_camelcase(prop))
                    self._to_xml(el, item)
                continue

            if isinstance(property, BaseResourceSimpleList):
                for item in property.items:
                    el = SubElement(elem, self._converter.to_camelcase(prop))
                    el.text = str(item)
                continue

            # Everything else

            el = SubElement(elem, self._converter.to_camelcase(prop))

            if isinstance(property, BaseMap):
                self._to_xml(el, property)
                if (len(el.getchildren()) == 0) and (el.text is None):
                    elem.remove(el)
            else:
                el.text = str(property)

        return elem

    def delete(self):
        response = self._client.delete(self.get_xpath())
        return response.status_code == HTTP_OK

    def get(self, id=None, params=None):
        return self._get_data(id, params)

    def get_status(self, id=None, params=None):
        return self._get_status(self.get_xpath(id), params)

    def get_xpath(self, save_path=False):
        parent_path = ""
        if self._parent is not None:
            parent_path = self._parent.get_xpath(save_path)
        own_path = self._xpath
        if save_path and (self._xpath_save is not None):
           own_path = self._xpath_save
        xpath = parent_path + own_path
        return xpath.format(self.id)

    def save(self):
        self._save()