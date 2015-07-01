from iris_sdk.models.account import Account
from iris_sdk.client import Client

class GetAvailableNumbers():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(self._client)

        print("\n--- Available numbers ---\n")

        available_numbers = \
            acc.available_numbers.list({"areaCode": "435"})

        print("total for search: " + acc.available_numbers.result_count)

        for phone_number in available_numbers.items:
            print(phone_number)

        print("\ndetailed list:\n")

        available_numbers_detail = acc.available_numbers.list(
            {"areaCode": "435", "enableTNDetail": "true"})
        for detail in available_numbers_detail.items:
            print(detail.full_number or "")
            print("    account: " + (detail.account_id or ""))
            print("    city: " + (detail.city or ""))
            print("    last modified: " + (detail.last_modified or ""))
            print("    LATA: " + (detail.lata or ""))
            print("    rate center: " + (detail.rate_center or ""))
            print("    state: " + (detail.state or ""))
            print("    status: " + (detail.status or ""))
            print("    tier: " + (detail.tier or ""))
            print("    vendor id: " + (detail.vendor_id or ""))
            print("    vendor name: " + (detail.vendor_name or ""))