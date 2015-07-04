from iris_sdk.models.account import Account
from iris_sdk.client import Client

class GetInServiceNumbers():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- In-service numbers ---\n")

        in_service_numbers = acc.in_service_numbers.list({"page":1,"size":20})

        print("Totals for search: " + \
            (acc.in_service_numbers.result_count or ""))

        for phone_number in in_service_numbers.items:
            print(phone_number.telephone_number)

        print("Numbers in service: " + \
            (acc.in_service_numbers.totals_count() or ""))