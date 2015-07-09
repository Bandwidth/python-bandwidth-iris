#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.error_list import ErrorList
from iris_sdk.models.data.ord.area_code_search_order import \
    AreaCodeSearchOrder
from iris_sdk.models.data.ord.city_search_order import \
    CitySearchOrder
from iris_sdk.models.data.ord.existing_search_order import \
    ExistingSearchOrder
from iris_sdk.models.data.ord.lata_search_order import \
    LataSearchOrder
from iris_sdk.models.data.ord.npa_search_order import \
    NpaSearchOrder
from iris_sdk.models.data.ord.rate_center_search_order import \
    RateCenterSearchOrder
from iris_sdk.models.data.ord.state_search_order import \
    StateSearchOrder
from iris_sdk.models.data.ord.vanity_search_order import \
    VanitySearchOrder
from iris_sdk.models.data.ord.wildcard_search_order import \
    WildcardSearchOrder
from iris_sdk.models.data.ord.zip_search_order import \
    ZipSearchOrder
from iris_sdk.models.maps.order import OrderMap

class OrderData(OrderMap, BaseData):

    def __init__(self):
        self.area_code_search_and_order_type = AreaCodeSearchOrder()
        self.city_search_and_order_type = CitySearchOrder()
        self.existing_telephone_number_order_type = ExistingSearchOrder()
        self.lata_search_and_order_type = LataSearchOrder()
        self.npanxx_search_and_order_type = NpaSearchOrder()
        self.rate_center_search_and_order_type = RateCenterSearchOrder()
        self.state_search_and_order_type = StateSearchOrder()
        self.toll_free_vanity_search_and_order_type = VanitySearchOrder()
        self.toll_free_wild_char_search_and_order_type = WildcardSearchOrder()
        self.zip_search_and_order_type = ZipSearchOrder()