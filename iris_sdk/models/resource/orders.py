#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.resource.order import OrderDetails
from iris_sdk.models.resource.data.orders.order_id_user_id_date import \
    OrderIdUserIdDate
from iris_sdk.models.base_resource import BaseResource, BaseResourceList

XML_NAME_ORDERS = "ListOrderIdUserIdDate"
XPATH_ORDERS = "/orders"

class OrdersData(object):

    @property
    def items(self):
        return self.order_id_user_id_date

    @property
    def order_id_user_id_date(self):
        return self._order_id_user_id_date

    @property
    def search_count(self):
        return self.total_count

    @property
    def total_count(self):
        return self._total_count
    @total_count.setter
    def total_count(self, total_count):
        self._total_count = total_count

class Orders(OrdersData, BaseResource):

    """Orders for account"""

    _xpath = XPATH_ORDERS
    _node_name = XML_NAME_ORDERS

    def __init__(self, client=None, xpath=None):
        super().__init__(client, xpath)
        self._order_id_user_id_date = BaseResourceList()
        self._total_count = None

    def clear(self):
        self._total_count = None
        del self._order_id_user_id_date.items[:]
        self._order_id_user_id_date.items.append(OrderIdUserIdDate())

    def list(self, params=None):
        self.clear()
        self.get_data(params=params)
        self.prepare_lists()
        return self.order_id_user_id_date.items

    def order(self, id=None):
        order = OrderDetails(self.client, self._xpath)
        return order.get(id=id)

    def prepare_lists(self):
        self._prepare_list(self._order_id_user_id_date.items)
        for details in self._order_id_user_id_date.items:
            self._prepare_list(details.telephone_number_details.cities_list)
            self._prepare_list(
                details.telephone_number_details.rate_centers_list)
            self._prepare_list(details.telephone_number_details.states_list)
            self._prepare_list(details.telephone_number_details.tiers_list)
            self._prepare_list(details.telephone_number_details.vendors_list)