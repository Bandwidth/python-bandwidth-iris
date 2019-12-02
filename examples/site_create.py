import sys

from iris_sdk import Account, Client, RestError

if len(sys.argv) < 2:
    sys.exit("usage: python site_create.py [site name], e.g.:\n" +
        "python site_create.py test12")

acc = Account(client=Client(filename="config.cfg"))

print("\n")

try:
    site = acc.sites.create({
        "name": sys.argv[1],
        "address": {
            "city": "Raleigh",
            "address_type": "Service",
            "house_number": "1",
            "street_name": "Avenue",
            "state_code": "NC",
            "zip": "27606"
        }
    })
except RestError as error:
    sys.exit(error)

print("id: " + (site.id or ""))
print("name: " + (site.name or ""))
print("address:")
print("    city: " + (site.address.city or ""))
print("    addr. type: " + (site.address.address_type or ""))
print("    house no.: " + (site.address.house_number or ""))
print("    street: " + (site.address.street_name or ""))
print("    state: " + (site.address.state_code or ""))

print("\nupdating site house number...")

site.address.house_number = "12"

try:
    site.save()
except RestError as error:
    sys.exit(error)

print("\nsuccess")
print("new house number: " + (site.address.house_number or ""))
