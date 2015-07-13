import sys

from iris_sdk import Account, Client, RestError

if len(sys.argv) < 2:
    sys.exit("usage: python order_get.py [order id], e.g.:" +
        "\npython order_get.py e2cbe50e-a23e-4bdc-b92b-00eff444ca17")

acc = Account(client=Client(filename="config.cfg"))

print("\n")

try:
    order = acc.orders.get(sys.argv[1]).order
except RestError as error:
    sys.exit(error)

print((order.name or ""))
print("    id: " + (order.id or ""))
print("    site: " + (order.site_id or ""))
print("    customer order id: " + (order.customer_order_id or ""))