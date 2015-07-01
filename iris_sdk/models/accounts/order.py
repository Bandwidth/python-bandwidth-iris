#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.resource.data.orders.completed_numbers import \
    CompletedNumbers
from iris_sdk.models.resource.data.orders.errors import ErrorList
from iris_sdk.models.resource.data.orders.order import Order
from iris_sdk.models.base_resource import BaseResource, BaseResourceList

XML_NAME_ORDER = "OrderResponse"
XPATH_ORDER = "/{}"

class OrderDetailsData(object):

    @property
    def completed(self):
        return self.completed_numbers.telephone_number

    @property
    def completed_numbers(self):
        return self._completed_numbers

    @property
    def completed_quantity(self):
        return self._completed_quantity
    @completed_quantity.setter
    def completed_quantity(self, completed_quantity):
        self._completed_quantity = completed_quantity

    @property
    def created_by_user(self):
        return self._created_by_user
    @created_by_user.setter
    def created_by_user(self, created_by_user):
        self._created_by_user = created_by_user

    @property
    def details(self):
        return self.order

    @property
    def error_list(self):
        return self._error_list

    @property
    def errors(self):
        return self.error_list.items

    @property
    def failed(self):
        return self.failed_numbers

    @property
    def failed_numbers(self):
        return self._failed_numbers

    @property
    def failed_quantity(self):
        return self._failed_quantity
    @failed_quantity.setter
    def failed_quantity(self, failed_quantity):
        self._failed_quantity = failed_quantity

    @property
    def last_modified_date(self):
        return self._last_modified_date
    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        self._last_modified_date = last_modified_date

    @property
    def order(self):
        return self._order

    @property
    def order_complete_date(self):
        return self._order_complete_date
    @order_complete_date.setter
    def order_complete_date(self, order_complete_date):
        self._order_complete_date = order_complete_date

    @property
    def order_status(self):
        return self._order_status
    @order_status.setter
    def order_status(self, order_status):
        self._order_status = order_status

    @property
    def pending_quantity(self):
        return self._pending_quantity
    @pending_quantity.setter
    def pending_quantity(self, pending_quantity):
        self._pending_quantity = pending_quantity

class OrderDetails(OrderDetailsData, BaseResource):

    """Order"""

    _xpath = XPATH_ORDER
    _node_name = XML_NAME_ORDER

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)
        self._completed_numbers = CompletedNumbers()
        self._completed_quantity = None
        self._created_by_user = None
        self._error_list = ErrorList()
        self._failed_numbers = []
        self._failed_quantity = None
        self._last_modified_date = None
        self._order = Order()
        self._order_complete_date = None
        self._order_status = None
        self._pending_quantity = None

    def clear(self):
        self._completed_quantity = None
        self._created_by_user = None
        self._failed_quantity = None
        del self._failed_numbers[:]
        self._last_modified_date = None
        self._order_complete_date = None
        self._order_status = None
        self._pending_quantity = None
        self._order.clear()
        self._completed_numbers.clear()
        self._error_list.clear()

    def get(self, id=None):
        self.clear()
        self.get_data(id=id)
        self._prepare_list(self._error_list.items)
        return self