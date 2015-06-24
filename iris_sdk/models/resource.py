#!/usr/bin/env python

from iris_sdk.utils.strings import Converter
from xml.etree import ElementTree

FOO_XML = (
    "<AccountResponse>"
    "<Account>"
    "    <AccountId>14</AccountId>"
    "    <CompanyName>CWI Hosting</CompanyName>"
    "    <AccountType>Business</AccountType>"
    "    <NenaId></NenaId>"
    "    <Tiers>"
    "        <Tier>0</Tier>"
    "    </Tiers>"
    "    <Address>"
    "        <HouseNumber>60</HouseNumber>"
    "        <HouseSuffix></HouseSuffix>"
    "        <PreDirectional></PreDirectional>"
    "        <StreetName>Pine</StreetName>"
    "        <StreetSuffix>St</StreetSuffix>"
    "        <PostDirectional></PostDirectional>"
    "        <AddressLine2></AddressLine2>"
    "        <City>Denver</City>"
    "        <StateCode>CO</StateCode>"
    "        <Zip>80016</Zip>"
    "        <PlusFour></PlusFour>"
    "        <County></County>"
    "        <Country>United States</Country>"
    "        <AddressType>Service</AddressType>"
    "    </Address>"
    "    <Contact>"
    "        <FirstName>Sanjay</FirstName>"
    "        <LastName>Rao</LastName>"
    "        <Phone>9195441234</Phone>"
    "        <Email>srao@bandwidth.com</Email>"
    "    </Contact>"
    "    <ReservationAllowed>true</ReservationAllowed>"
    "    <LnpEnabled>true</LnpEnabled>"
    "    <AltSpid>X455</AltSpid>"
    "    <SPID>9999</SPID>"
    "    <PortCarrierType>WIRELINE</PortCarrierType>"
    "</Account>"
    "</AccountResponse>"
)

class BaseResource():

    """REST resource"""

    def __init__(self, client=None):

        self._client = client
        self._id = None
        self._xpath = None
        self._converter = Converter()

    # TODO: back - object to xml
    def _parse_xml(self, element=None, instance=None):

        """
        Parses XML elements into existing objects, e.g.:

        garply = foo()
        <Foo><BarBaz>Qux</Bar></Foo> -> a.bar_baz equals "qux".

        Converts lowercase names to CamelCase.
        """

        inst = (self if instance is None else instance)
        base_class = inst.__class__
        class_name = self._converter.to_camelcase(base_class.__name__)
        element_children = element.findall(class_name)
        for el in element_children:
            tags = el.getchildren()
            for prop in tags:
                tag = self._converter.to_underscore(prop.tag)
                if hasattr(base_class, tag):
                    if (len(prop.getchildren()) == 0):
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
    def id(self):
        return self._id

    def get(self, id, params=None):
        #response_str = self._client.get(id, self._xpath.format(id), params)
        response_str = FOO_XML
        root = ElementTree.fromstring(response_str)
        self._parse_xml(root)

class BaseList(BaseResource):

    """A collection of resources"""

    pass