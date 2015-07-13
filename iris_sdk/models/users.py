#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.password import Password

XPATH_USERS = "/users/{}"

class Users(BaseResource):

    """System users"""

    _xpath = XPATH_USERS

    @property
    def password(self):
        return self._password

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        if client is not None:
            self.id = (client.config.username or "")
        self._password = Password(self, client)