import sys

from iris_sdk import Client, Tns, RestError

if len(sys.argv) < 2:
    sys.exit("usage: python tns_details.py [number], e.g.:" +
        "\npython tns_details.py 4109235436")

tns = Tns(client=Client(filename="config.cfg"))

print("\n")

try:
    details = tns.get(sys.argv[1]).tndetails.get()
except RestError as error:
    sys.exit(error)

print("    account: " + (details.account_id or ""))
print("    city: " + (details.city or ""))
print("    last modified: " + (details.last_modified_date or ""))
print("    LATA: " + (details.lata or ""))
print("    rate center: " + (details.rate_center or ""))
print("    state: " + (details.state or ""))
print("    tier: " + (details.tier or ""))
print("    vendor id: " + (details.vendor_id or ""))
print("    vendor name: " + (details.vendor_name or ""))

print("    dlda")
print("        city: " + (details.features.dlda.address.city or ""))
print("        listing: ")
print("            first name" +
    (details.features.dlda.listing_name.first_name or ""))
print("            last name" + \
    (details.features.dlda.listing_name.last_name or ""))
print("    lidb")
print("        status: " + (details.features.lidb.status or ""))