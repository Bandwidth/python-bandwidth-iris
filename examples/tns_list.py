import sys

from iris_sdk import Client, Tns, RestError

if len(sys.argv) < 2:
    sys.exit("usage: python tns_list.py [npa], e.g.:\npython tns_list.py 818")

tns = Tns(client=Client(filename="config.cfg"))

print("\n")

try:
    tn_list = tns.list({"page": 1, "size": 10, "npa": sys.argv[1]})
except RestError as error:
    sys.exit(error)

for phone in tn_list.items:
    print(phone.full_number or "")
    print("    account: " + (phone.account_id or ""))
    print("    city: " + (phone.city or ""))
    print("    last modified: " + (phone.last_modified_date or ""))
    print("    LATA: " + (phone.lata or ""))
    print("    rate center: " + (phone.rate_center or ""))
    print("    state: " + (phone.state or ""))
    print("    status: " + (phone.status or ""))
    print("    vendor id: " + (phone.vendor_id or ""))
    print("    vendor name: " + (phone.vendor_name or ""))