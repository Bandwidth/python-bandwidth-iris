#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.email_subscription import EmailSubscription
from iris_sdk.models.data.callback_subscription import CallbackSubscription
from iris_sdk.models.maps.subscription import SubscriptionMap

class SubscriptionData(SubscriptionMap, BaseData):

    def __init__(self):
        self.email_subscription = EmailSubscription()
        self.callback_subscription = CallbackSubscription()