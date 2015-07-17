#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.subscription_response import SubscriptionResponseMap

class SubscriptionResponseData(SubscriptionResponseMap, BaseData):
    pass