#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.subscription import SubscriptionData

XPATH_SUBSCRIPTION = "/{}"

class Subscription(BaseResource, SubscriptionData):

    """Subscription for account"""

    _xpath = XPATH_SUBSCRIPTION

    @property
    def id(self):
        return self.subscription_id
    @id.setter
    def id(self, id):
        self.subscription_id = id

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SubscriptionData.__init__(self)

    def get(self, id=None):
        return self._get_data(id)