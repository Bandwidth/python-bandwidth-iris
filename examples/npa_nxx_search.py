import sys

from iris_sdk import Account, Client

if len(sys.argv) < 3:
    sys.exit("usage: python npa_nxx_search.py [area code] [quantity], e.g.:" +
        "\npython npa_nxx_search.py 435 1")

acc = Account(client=Client(filename="config.cfg"))

available_npa = acc.available_npa_nxx.list(
    {"areaCode": sys.argv[1], "quantity": sys.argv[2]})

for phone_number in available_npa.items:
    print(" - ")
    print("    city: " + (phone_number.city or ""))
    print("    NPA: " + (phone_number.npa or ""))
    print("    NXX: " + (phone_number.nxx or ""))
    print("    state: " + (phone_number.state or ""))
    print("    quantity: " + (phone_number.quantity or ""))