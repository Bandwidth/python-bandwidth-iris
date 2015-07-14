#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.callback_subscription import CallbackSubscriptionMap

class CallbackSubscription(CallbackSubscriptionMap, BaseData):
    pass