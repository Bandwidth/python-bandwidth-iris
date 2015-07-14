#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceList
from iris_sdk.models.maps.subscriptions import SubscriptionsMap
from iris_sdk.models.subscription import Subscription

class SubscriptionsData(SubscriptionsMap, BaseData):

    def __init__(self, parent=None):
        self.subscription = BaseResourceList(Subscription, parent)