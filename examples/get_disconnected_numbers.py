from iris_sdk.models.account import Account
from iris_sdk.client import Client

class GetDisconnectedNumbers():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- Disconnected numbers ---\n")

        disc_numbers = \
            acc.disconnected_numbers.list({"page": 1, "size": 20})

        print("total for search: " + \
            (acc.disconnected_numbers.result_count or "0"))

        for phone_number in disc_numbers.items:
            print(phone_number.telephone_number)