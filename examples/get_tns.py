from iris_sdk.models.tns import Tns
from iris_sdk.client import Client

class GetTns():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        tns = Tns(client=self._client)

        print("\n--- TNs ---\n")

        phone_numbers = tns.list({"page": "1", "size": 20})

        print("total for search: " + (tns.result_count or "") + "\n")

        for phone_number in phone_numbers.items:
            print(phone_number.full_number or "")
            print("    account: " + (phone_number.account_id or ""))
            print("    city: " + (phone_number.city or ""))
            print("    last modified: " + \
                (phone_number.last_modified_date or ""))
            print("    LATA: " + (phone_number.lata or ""))
            print("    rate center: " + (phone_number.rate_center or ""))
            print("    state: " + (phone_number.state or ""))
            print("    status: " + (phone_number.status or ""))
            print("    vendor id: " + (phone_number.vendor_id or ""))
            print("    vendor name: " + (phone_number.vendor_name or ""))

        phone = tns.get(7576768750)

        print("\n")
        print(phone.id or "")
        print("    order created: " + (phone.order_create_date or ""))