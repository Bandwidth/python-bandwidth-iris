#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.email_subscription import EmailSubscriptionMap

class EmailSubscription(EmailSubscriptionMap, BaseData):
    pass