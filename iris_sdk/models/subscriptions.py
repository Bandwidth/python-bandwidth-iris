#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.subscriptions import SubscriptionsData
from iris_sdk.models.subscription import Subscription

XPATH_SUBSCRIPTIONS = "/subscriptions"

class Subscriptions(BaseResource, SubscriptionsData):

    """Subscriptions for account"""

    _xpath = XPATH_SUBSCRIPTIONS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SubscriptionsData.__init__(self, self)

    def create(self, data=None, save=True):
        subscription = Subscription(self).set_from_dict(data)
        if save and (data is not None):
            subscription.save()
        return subscription

    def get(self, id, params=None):
        return Subscription(self).get(id, params=params)

    def list(self):
        return self._get_data().subscription