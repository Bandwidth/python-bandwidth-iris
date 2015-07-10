from iris_sdk.models.account import Account
from iris_sdk.client import Client

class Pagination():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- In-service numbers pagination ---\n")

        in_service_numbers = acc.in_service_numbers.list({"page":1,"size":10})

        total_displayed = len(in_service_numbers.items)
        total = int(acc.in_service_numbers.result_count)

        page = None
        while (total_displayed <= total):
            if (page is not None):
                in_service_numbers = acc.in_service_numbers.list(
                    {"page": page, "size": 10})
            page = acc.in_service_numbers.links.next
            for phone_number in in_service_numbers.items:
                print(phone_number.telephone_number)
            total_displayed += len(in_service_numbers.items)