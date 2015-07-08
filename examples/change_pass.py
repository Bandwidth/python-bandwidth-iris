from iris_sdk.client import Client
from iris_sdk.models.users import Users
from iris_sdk.utils.rest import RestError

class ChangePass():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        users = Users(client=self._client)

        print("\n--- Changing password ---\n")

        try:
            users.password.change("1")
        except RestError as error:
            print(error)