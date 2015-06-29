from iris_sdk.models.accounts import Account
from iris_sdk.client import Client

class GetInServiceNumbersExample():

    def __init__(self, url=None, account_id=None, username=None,
            password=None, filename=None):

        self._client = Client(
            url=url,
            account_id=account_id,
            username=username,
            password=password
        )

        acc = Account(self._client)

        print("\n--- In-service numbers ---\n")

        in_service_numbers = acc.in_service_numbers.list({"page":1, "size":1})

        i = 1
        total_displayed = len(in_service_numbers)
        total = int(acc.in_service_numbers.search_count)

        print("total for search: " + acc.in_service_numbers.search_count)

        while (total_displayed <= total):
            if (i > 1):
                in_service_numbers = acc.in_service_numbers.list(
                    {"page": i, "size": 1})
            for phone_number in in_service_numbers:
                print(phone_number)
            i += 1
            total_displayed += len(in_service_numbers)

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