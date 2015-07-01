#!/usr/bin/env python

class TelephoneNumberData(object):

    @property
    def account_id(self):
        return self._account_id
    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

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
    def last_modified(self):
        return self._last_modified
    @last_modified.setter
    def last_modified(self, last_modified):
        self._last_modified = last_modified

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
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        self._status = status

    @property
    def telephone_number(self):
        return self._full_number
    @telephone_number.setter
    def telephone_number(self, telephone_number):
        self._full_number = telephone_number

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

class TelephoneNumber(TelephoneNumberData):

    def __init__(self):
        self.clear()

    def clear(self):
        self.account_id = None
        self.city = None
        self.full_number = None
        self.last_modified = None
        self.lata = None
        self.rate_center = None
        self.state = None
        self.status = None
        self.tier = None
        self.vendor_id = None
        self.vendor_name = None