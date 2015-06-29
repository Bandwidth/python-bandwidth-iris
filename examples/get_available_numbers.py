from iris_sdk.models.accounts import Account
from iris_sdk.client import Client

class GetAvailableNumbersExample():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(self._client)

        print("\n--- Available numbers ---\n")

        available_numbers = \
            acc.available_numbers.list({"areaCode": "435"})

        print("total for search: " + acc.available_numbers.search_count)

        for phone_number in available_numbers:
            print(phone_number)

        print("\ndetailed list:\n")

        available_numbers_detail = acc.available_numbers.list(
            {"areaCode": "435", "enableTNDetail": "true"})
        for detail in available_numbers_detail:
            print(detail.full_number)
            print("    city: " + detail.city)
            print("    LATA: " + detail.lata)
            print("    rate center: " + detail.rate_center)
            print("    state: " + detail.state)
            print("    tier: " + detail.tier)
            print("    vendor id: " + detail.vendor_id)
            print("    vendor name: " + detail.vendor_name)