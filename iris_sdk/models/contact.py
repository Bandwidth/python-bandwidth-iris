#!/usr/bin/env python

from abc import ABC

class ContactData(ABC):

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, phone):
        self._phone = phone

class Contact(ContactData):

    def __init__(self):
        self._email = None
        self._first_name = None
        self._last_name = None
        self._phone = None