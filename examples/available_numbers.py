import sys

from iris_sdk import Account, Client, RestError

if len(sys.argv) < 3:
    sys.exit("usage: python available_numbers.py [state] [quantity], e.g.:" +
        "\npython available_numbers.py NJ 3")

acc = Account(client=Client(filename="config.cfg"))

print("\n")

try:
    available_numbers = acc.available_numbers.list(
        {"state": sys.argv[1], "quantity": sys.argv[2]})
except RestError as error:
    sys.exit(error)

print("\nTotal for search: " + (acc.available_numbers.result_count or ""))

for phone_number in available_numbers.items:
    print(phone_number or "")