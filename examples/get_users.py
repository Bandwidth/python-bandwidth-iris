from iris_sdk.client import Client
from iris_sdk.models.account import Account

class GetUsers():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- Users ---\n")

        users = acc.users.list()

        for user in users.items:

            print("username: " + (user.username or ""))
            print("first name: " + (user.first_name or ""))
            print("last name: " + (user.last_name or ""))
            print("email: " + (user.email_address or ""))
            print("phone no.: " + (user.telephone_number or ""))

            print("roles:")
            for role in user.roles.items:
                print("    " + (role.name or ""))
                print("        permissions:")
                for permission in role.permissions.items:
                    print("            " + (permission.name))