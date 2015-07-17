#!/usr/bin/env python

import os
import sys

# For coverage.
if __package__ is None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from unittest import main, TestCase

import requests
import requests_mock

from iris_sdk.client import Client
from iris_sdk.models.account import Account
from iris_sdk.models.users import Users

XML_RESPONSE_USERS_LIST = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<UsersResponse><Users><User><Username>byo_dev</Username>"
    "<FirstName>test</FirstName><LastName>test</LastName>"
    "<EmailAddress>jsommerset@bandwidth.com</EmailAddress>"
    "<TelephoneNumber>5413637598</TelephoneNumber><Roles><Role>"
    "<RoleName>ROLE_USER</RoleName><Permissions><Permission>"
    "<PermissionName>UPDATE</PermissionName></Permission><Permission>"
    "<PermissionName>VIEW</PermissionName></Permission></Permissions>"
    "</Role><Role><RoleName>ROLE_BDR</RoleName><Permissions><Permission>"
    "<PermissionName>UPDATE</PermissionName></Permission><Permission>"
    "<PermissionName>VIEW</PermissionName></Permission></Permissions>"
    "</Role><Role><RoleName>ROLE_API_HISTORY</RoleName><Permissions>"
    "<Permission><PermissionName>UPDATE</PermissionName></Permission>"
    "<Permission><PermissionName>VIEW</PermissionName></Permission>"
    "</Permissions></Role><Role><RoleName>ROLE_API_SITE</RoleName>"
    "<Permissions><Permission><PermissionName>UPDATE</PermissionName>"
    "</Permission><Permission><PermissionName>VIEW</PermissionName>"
    "</Permission></Permissions></Role>"
    "<Role><RoleName>ROLE_API_SEARCH</RoleName><Permissions>"
    "<Permission><PermissionName>VIEW</PermissionName></Permission>"
    "</Permissions></Role><Role><RoleName>ROLE_API_ORDERING</RoleName>"
    "<Permissions><Permission><PermissionName>UPDATE</PermissionName>"
    "</Permission><Permission><PermissionName>VIEW</PermissionName>"
    "</Permission></Permissions></Role><Role>"
    "<RoleName>ROLE_API_PROFILE</RoleName><Permissions><Permission>"
    "<PermissionName>UPDATE</PermissionName></Permission><Permission>"
    "<PermissionName>VIEW</PermissionName></Permission></Permissions>"
    "</Role><Role><RoleName>ROLE_API_LNP</RoleName><Permissions>"
    "<Permission><PermissionName>UPDATE</PermissionName></Permission>"
    "<Permission><PermissionName>VIEW</PermissionName></Permission>"
    "</Permissions></Role><Role><RoleName>ROLE_API_ACCOUNT</RoleName>"
    "<Permissions><Permission><PermissionName>VIEW</PermissionName>"
    "</Permission></Permissions></Role>"
    "<Role><RoleName>ROLE_API_DLDA</RoleName><Permissions><Permission>"
    "<PermissionName>UPDATE</PermissionName></Permission><Permission>"
    "<PermissionName>VIEW</PermissionName></Permission></Permissions>"
    "</Role><Role><RoleName>ROLE_API_CNAMLIDB</RoleName><Permissions>"
    "<Permission><PermissionName>UPDATE</PermissionName></Permission>"
    "<Permission><PermissionName>VIEW</PermissionName></Permission>"
    "</Permissions></Role></Roles></User></Users></UsersResponse>"
)

class ClassUsersTest(TestCase):

    """Test the Users directory"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._account
        del cls._client

    def test_change_pass(self):

        with requests_mock.Mocker() as m:

            users = Users(client=self._client)

            url = self._client.config.url + users.password.get_xpath()
            m.put(url)
            
            users.password.change("foobar")

    def test_users_list(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._account.users.get_xpath()
            m.get(url, content=XML_RESPONSE_USERS_LIST)
            
            user = self._account.users.list().items[0]

            self.assertEqual(user.username, "byo_dev")
            self.assertEqual(user.first_name, "test")
            self.assertEqual(user.last_name, "test")
            self.assertEqual(user.email_address, "jsommerset@bandwidth.com")
            self.assertEqual(user.telephone_number, "5413637598")
            self.assertEqual(user.roles.role.items[0].role_name, "ROLE_USER")
            self.assertEqual(
                user.roles.role.items[0].permissions.\
                    permission.items[0].permission_name,
                "UPDATE")

if __name__ == "__main__":
    main()