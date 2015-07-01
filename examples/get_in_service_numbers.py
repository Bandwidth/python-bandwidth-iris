from iris_sdk.models.account import Account
from iris_sdk.client import Client

class GetInServiceNumbers():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(self._client)

        print("\n--- In-service numbers ---\n")

        in_service_numbers = acc.in_service_numbers.list({"page":1, "size":1})

        total_displayed = len(in_service_numbers.items)
        total = int(acc.in_service_numbers.result_count)

        print("total for search: " + acc.in_service_numbers.result_count)

        page = None
        while (total_displayed <= total):
            if (page is not None):
                in_service_numbers = acc.in_service_numbers.list(
                    {"page": page, "size": 1})
            page = acc.in_service_numbers.links.next
            for phone_number in in_service_numbers.items:
                print(phone_number.telephone_number)
            total_displayed += len(in_service_numbers.items)

        print("total numbers for account: " + \
            acc.in_service_numbers.totals_count())
        print("Veryfying number " + "8183386252")
        print("    .")
        print("    .")
        print("    .")
        print("    .")
        print("    .")
        print("    .")
        print("    .")
        print("    .")

        try:
            if (acc.in_service_numbers.verify(8183386252) == 200):
                print("ok")
        except:
            print("not found")