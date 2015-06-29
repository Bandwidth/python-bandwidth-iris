from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.resource.data.orders.telephone_number_details import \
    TelephoneNumberDetails

class OrderIdUserIdDateData(object):

    @property
    def count_of_t_ns(self):
        return self._count_of_t_ns
    @count_of_t_ns.setter
    def count_of_t_ns(self, count_of_t_ns):
        self._count_of_t_ns = count_of_t_ns

    @property
    def count_of_tns(self):
        return self.count_of_t_ns

    @property
    def customer_order_id(self):
        return self._customer_order_id
    @customer_order_id.setter
    def customer_order_id(self, customer_order_id):
        self._customer_order_id = customer_order_id

    @property
    def last_modified_date(self):
        return self._last_modified_date
    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        self._last_modified_date = last_modified_date

    @property
    def order_date(self):
        return self._order_date
    @order_date.setter
    def order_date(self, order_date):
        self._order_date = order_date

    @property
    def order_id(self):
        return self._order_id
    @order_id.setter
    def order_id(self, order_id):
        self._order_id = order_id

    @property
    def order_status(self):
        return self._order_status
    @order_status.setter
    def order_status(self, order_status):
        self._order_status = order_status

    @property
    def order_type(self):
        return self._order_type
    @order_type.setter
    def order_type(self, order_type):
        self._order_type = order_type

    @property
    def telephone_number_details(self):
        return self._telephone_number_details

    @property
    def user_id(self):
        return self._user_id
    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

class OrderIdUserIdDate(OrderIdUserIdDateData):

    def __init__(self):
        self._count_of_t_ns = None
        self._customer_order_id = None
        self._last_modified_date = None
        self._order_date = None
        self._order_id = None
        self._order_status = None
        self._order_type = None
        self._user_id = None
        self._telephone_number_details = TelephoneNumberDetails()