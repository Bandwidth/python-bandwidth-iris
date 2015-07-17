import sys

from iris_sdk import Account, Client, RestError

if len(sys.argv) < 2:
    sys.exit("usage: python order_create.py [phone number], e.g.:" +
        "\npython order_create.py 9193752369")

acc = Account(client=Client(filename="config.cfg"))

print("\n")

try:
    order = acc.orders.create({
        "name": "Available telephone number order",
        "site_id": "2297",
        "customer_order_id": "123456789",
        "existing_telephone_number_order_type": {
            "telephone_number_list": {
                "telephone_number": [sys.argv[1]]
            }
        }
    })
except RestError as error:
    sys.exit(error)

print((order.name or "") + " (" + (order.order_status or "") + ")")
print("    id: " + (order.id or ""))
print("    site: " + (order.site_id or ""))
print("    customer order id: " + (order.customer_order_id or ""))
print("    phone numbers:")
for num in order.existing_telephone_number_order_type.telephone_number_list.\
        telephone_number.items:
    print("       " + (num or ""))