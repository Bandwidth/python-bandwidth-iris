#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource

XPATH_PASSWORD = "/password"
PAYLOAD_PASSWORD = "<Password>{}</Password>"

class Password(BaseResource):

    """Changing user's pass"""

    _xpath = XPATH_PASSWORD

    def change(self, new_password):
        self._put_data(self.get_xpath(),
            PAYLOAD_PASSWORD.format(new_password))