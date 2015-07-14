#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.dlda_tn_group import DldaTnGroupMap
from iris_sdk.models.data.telephone_number_list import TelephoneNumberList
from iris_sdk.models.data.address import Address
from iris_sdk.models.data.listing_name import ListingName

class DldaTnGroupData(DldaTnGroupMap, BaseData):

    telephone_numbers = TelephoneNumberList()
    listingName = ListingName()
    address = Address()