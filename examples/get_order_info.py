from iris_sdk.models.accounts import Account
from iris_sdk.client import Client

class GetOrderInfoExample():

    def __init__(self, url=None, account_id=None, username=None,
            password=None, filename=None):

        self._client = Client(
            url=url,
            account_id=account_id,
            username=username,
            password=password
        )

        acc = Account(self._client)

        print("\n--- Order e2cbe50e-a23e-4bdc-b92b-00eff444ca17 ---\n")

# Completed
#order = acc.orders.order("e2cbe50e-a23e-4bdc-b92b-00eff444ca17")
# Failed
order = acc.orders.order("15b6fa5f-da6e-47a3-8cb1-f2ee4ca36ea9")

print("name: " + (order.details.name or ""))
print("customer order: " + (order.details.customer_order_id or ""))
print("created by: " + (order.created_by_user or ""))
print("completed quantity: " + (order.completed_quantity or ""))
print("complete date: " + (order.order_complete_date or ""))
print("failed: " + (order.failed_quantity or ""))

print("completed numbers:")
for number in order.completed:
    print("    " + (number or ""))

print("search and order:")
search_and_order = order.details.area_search
print("    area code: " + (search_and_order.area_code or ""))
print("    quantity: " + (search_and_order.quantity or ""))

print("failed numbers:")
for number in order.failed:
    print("    " + (number or ""))

print("errors:")
for error in order.errors:
    print("    code: " + (error.code or ""))
    print("        info: " + (error.description or ""))
    print("        tn: " + (error.telephone_number or ""))