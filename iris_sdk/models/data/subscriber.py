#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.address import Address
from iris_sdk.models.maps.subscriber import SubscriberMap

class Subscriber(SubscriberMap, BaseData):

    def __init__(self):
        self.service_address = Address()