#!/usr/bin/env python

from iris_sdk.models.maps.base_map import BaseMap

class SubscriptionMap(BaseMap):

    subscription_id = None
    order_id = None
    order_type = None
    email_subscription = None
    callback_subscription = None