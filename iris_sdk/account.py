#!/usr/bin/env python

from iris_sdk.models.resource import BaseResource
from iris_sdk.models.address import Address

class Account(BaseResource):

    """Iris account"""

    def __init__(self, client=None):
        super().__init__(client)
        self._address = Address()

    @property
    def address(self):
        return self._address = address
    @address.setter(self, address):
        self._address = address

    @property
    def customer_name(self):
        return self._customer_name
    @customer_name.setter
    def customer_name(self, customer_name):
        self._customer_name = customer_name

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name