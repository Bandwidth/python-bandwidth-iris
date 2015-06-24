#!/usr/bin/env python

class Address():

    def __init__(self):
        self._address = None
        self._city = None
        self._country = None
        self._house_number = None
        self._state_code = None
        self._street_name = None

    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, address):
        self._address = address

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, city):
        self._city = city

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