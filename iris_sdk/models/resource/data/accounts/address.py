#!/usr/bin/env python

#from abc import ABC

class AddressData(object):

    @property
    def address_line2(self):
        return self._address_line2
    @address_line2.setter
    def address_line2(self, address_line2):
        self._address_line2 = address_line2

    @property
    def address_type(self):
        return self._address_type
    @address_type.setter
    def address_type(self, address_type):
        self._address_type = address_type

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, city):
        self._city = city

    @property
    def county(self):
        return self._county
    @county.setter
    def county(self, county):
        self._county = county

    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, country):
        self._country = country

    @property
    def house_number(self):
        return self._house_number
    @house_number.setter
    def house_number(self, house_number):
        self._house_number = house_number

    @property
    def house_suffix(self):
        return self._house_suffix
    @house_suffix.setter
    def house_suffix(self, house_suffix):
        self._house_suffix = house_suffix

    @property
    def plus_four(self):
        return self._plus_four
    @plus_four.setter
    def plus_four(self, plus_four):
        self._plus_four = plus_four

    @property
    def pre_directional(self):
        return self._pre_directional
    @pre_directional.setter
    def pre_directional(self, pre_directional):
        self._pre_directional = pre_directional

    @property
    def post_directional(self):
        return self._post_directional
    @post_directional.setter
    def post_directional(self, post_directional):
        self._post_directional = post_directional

    @property
    def state_code(self):
        return self._state_code
    @state_code.setter
    def state_code(self, state_code):
        self._state_code = state_code

    @property
    def street_name(self):
        return self._street_name
    @street_name.setter
    def street_name(self, street_name):
        self._street_name = street_name

    @property
    def street_suffix(self):
        return self._street_suffix
    @street_suffix.setter
    def street_suffix(self, street_suffix):
        self._street_suffix = street_suffix

    @property
    def zip(self):
        return self._zip
    @zip.setter
    def zip(self, zip):
        self._zip = zip

class Address(AddressData):

    def __init__(self):
        self._address_line2 = None
        self._address_type = None
        self._city = None
        self._county = None
        self._country = None
        self._house_number = None
        self._house_suffix = None
        self._plus_four = None
        self._pre_directional = None
        self._post_directional = None
        self._state_code = None
        self._street_name = None
        self._street_suffix = None
        self._zip = None