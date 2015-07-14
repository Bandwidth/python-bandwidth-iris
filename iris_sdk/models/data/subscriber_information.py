#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData, BaseResourceSimpleList
from iris_sdk.models.maps.subscriber_information import SubscriberInformationMap

class SubscriberInformation(SubscriberInformationMap, BaseData):

    @property
    def items(self):
        return self.subscriber_information.items

    def __init__(self):
        self.subscriber_information = BaseResourceSimpleList()

    def add(self, phone_number=None):
        return self.subscriber_information.add(phone_number)