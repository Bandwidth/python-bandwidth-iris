import sys

from iris_sdk import Account, Client, RestError

if len(sys.argv) < 2:
    sys.exit("usage: python portin.py [8183386247], e.g.:" +
        "\npython portin.py 8183386247")

acc = Account(client=Client(filename="config.cfg"))
port_number = sys.argv[1]

print("\n")

try:
    response = acc.lnpchecker([port_number], "true")
except RestError as error:
    sys.exit(error)

if port_number not in response.portable_numbers.items:
    sys.exit()

print("Number is portable, creating LNP order")
print(acc._converter.to_underscore("CountOfTNs"))