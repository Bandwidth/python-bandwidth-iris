#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.subscription_response import SubscriptionResponseData

XML_NAME_SUBSCRIPTION_RESPONSE = "Subscriptions"
XPATH_SUBSCRIPTION_RESPONSE = "/{}"

class SubscriptionResponse(BaseResource, SubscriptionResponseData):

    """Account subscription response"""

    _node_name = XML_NAME_SUBSCRIPTION_RESPONSE
    _xpath = XPATH_SUBSCRIPTION_RESPONSE

    @property
    def id(self):
        return self.subscription.subscription_id
    @id.setter
    def id(self, subscription_id):
        self.subscription.subscription_id = subscription_id

    @property
    def subscription(self):
        return self._subscription
    @subscription.setter
    def subscription(self, subscription):
        self._subscription = subscription

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        SubscriptionResponseData.__init__(self)

    def get(self, id=None, params=None):
        return self._get_data((id or self.id), params=params)