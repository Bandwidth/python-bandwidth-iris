from iris_sdk.models.account import Account
from iris_sdk.client import Client

class WriteOrders():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- Ordering phones ---\n")

        order = acc.orders.add()
        order.site_id = 2297
        order.customer_order_id = 1337

        available_numbers = \
            acc.available_numbers.list({"areaCode": "435"})

        phone_number = available_numbers.items[0]
        if (phone_number is None):
            print("No available numbers")
            return

        print("ordering tn" + (phone_number.telephone_number or "") + " ...")
        order.add_tn(phone_number.telephone_number)
        id = order.save()
        print("ok, id: " + (order.id or ""))