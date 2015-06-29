#!/usr/bin/env python

class TelephoneNumberDetailData(object):

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, city):
        self._city = city

    @property
    def full_number(self):
        return self._full_number
    @full_number.setter
    def full_number(self, full_number):
        self._full_number = full_number

    @property
    def lata(self):
        return self._lata
    @lata.setter
    def lata(self, lata):
        self._lata = lata

    @property
    def rate_center(self):
        return self._rate_center
    @rate_center.setter
    def rate_center(self, rate_center):
        self._rate_center = rate_center

    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, state):
        self._state = state

    @property
    def tier(self):
        return self._tier
    @tier.setter
    def tier(self, tier):
        self._tier = tier

    @property
    def vendor_id(self):
        return self._vendor_id
    @vendor_id.setter
    def vendor_id(self, vendor_id):
        self._vendor_id = vendor_id

    @property
    def vendor_name(self):
        return self._vendor_name
    @vendor_name.setter
    def vendor_name(self, vendor_name):
        self._vendor_name = vendor_name

class TelephoneNumberDetail(TelephoneNumberDetailData):

    def __init__(self):
        self._city = None
        self._full_number = None
        self._lata = None
        self._rate_center = None
        self._state = None
        self._tier = None
        self._vendor_id = None
        self._vendor_name = None