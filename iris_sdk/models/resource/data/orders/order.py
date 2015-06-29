#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.resource.data.orders.area_search import \
    AreaCodeSearchAndOrderType
from iris_sdk.models.resource.data.orders.rate_search import \
    RateCenterSearchAndOrderType

class OrderData(object):

    @property
    def area_code_search_and_order_type(self):
        return self._area_code_search_and_order_type

    @property
    def area_search(self):
        return self.area_code_search_and_order_type

    @property
    def back_order_requested(self):
        return self._back_order_requested
    @back_order_requested.setter
    def back_order_requested(self, back_order_requested):
        self._back_order_requested = back_order_requested

    @property
    def customer_order_id(self):
        return self._customer_order_id
    @customer_order_id.setter
    def customer_order_id(self, customer_order_id):
        self._customer_order_id = customer_order_id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def order_created_date(self):
        return self._order_created_date
    @order_created_date.setter
    def order_created_date(self, order_created_date):
        self._order_created_date = order_created_date

    @property
    def partial_allowed(self):
        return self._partial_allowed
    @partial_allowed.setter
    def partial_allowed(self, partial_allowed):
        self._partial_allowed = partial_allowed

    @property
    def peer_id(self):
        return self._peer_id
    @peer_id.setter
    def peer_id(self, peer_id):
        self._peer_id = peer_id

    @property
    def rate_center_search_and_order_type(self):
        return self._rate_center_search_and_order_type

    @property
    def rate_center_search(self):
        return self.rate_center_search_and_order_type

    @property
    def tn_attributes(self):
        return self._tn_attributes

    @property
    def site_id(self):
        return self._site_id
    @site_id.setter
    def site_id(self, site_id):
        self._site_id = site_id

class Order(OrderData):

    def __init__(self):
        self._area_code_search_and_order_type = AreaCodeSearchAndOrderType()
        self._back_order_requested = None
        self._customer_order_id = None
        self._name = None
        self._order_created_date = None
        self._partial_allowed = None
        self._peer_id = None
        self._rate_center_search_and_order_type=RateCenterSearchAndOrderType()
        self._tn_attributes = []
        self._site_id = None

    def clear(self):
        self._area_code_search_and_order_type.clear()
        self._rate_center_search_and_order_type.clear()
        self._back_order_requested = None
        self._customer_order_id = None
        self._name = None
        self._order_created_date = None
        self._partial_allowed = None
        self._peer_id = None
        del self._tn_attributes[:]
        self._site_id = None