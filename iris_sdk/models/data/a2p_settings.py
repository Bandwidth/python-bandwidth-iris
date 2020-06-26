#!/usr/bin/env python
  
from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.a2p_settings import A2pSettingsMap

class A2pSettings(A2pSettingsMap, BaseData):
    pass
