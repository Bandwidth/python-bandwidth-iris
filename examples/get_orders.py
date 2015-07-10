from iris_sdk.models.account import Account
from iris_sdk.client import Client

class GetOrders():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- Orders ---\n")

        orders = acc.orders.list({"page": 1, "size": 10})

        for order in orders.items:
            print(order.id or "")
            print("    TN count: " + (order.count_of_tns or ""))
            print("    customer order id: " + (order.customer_order_id or ""))
            print("    user: " + (order.user_id or ""))
            print("    type: " + (order.order_type or ""))
            print("    status: " + (order.order_status or ""))