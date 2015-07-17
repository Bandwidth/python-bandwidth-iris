import sys

from iris_sdk import Account, Client, RestError

if len(sys.argv) < 3:
    sys.exit("usage: python portin.py [phone number] [site id], e.g.:" +
        "\npython portin.py 8183386247 2297")

acc = Account(client=Client(filename="config.cfg"))
port_number = sys.argv[1]

print("\n")

try:
    response = acc.lnpchecker([port_number], "true")
except RestError as error:
    sys.exit(error)

if port_number not in response.portable_numbers.items:
    sys.exit("Number isn't portable")

print("Number is portable, creating LNP order")

try:
    portin = acc.portins.create({
        "billing_telephone_number": port_number,
        "subscriber": {
            "subscriber_type": "BUSINESS",
            "business_name": "Acme Corporation",
            "service_address": {
                "house_number": "1623",
                "street_name": "Brockton Ave",
                "city": "Los Angeles",
                "state_code": "CA",
                "zip": "90025",
                "country": "USA"
            }
        },
        "loa_authorizing_person": "John Doe",
        "list_of_phone_numbers": {
            "phone_number": [port_number]
        },
        "site_id": sys.argv[2],
        "triggered": "false"
    })
except RestError as error:
    sys.exit(error)

print("Order created: " + (portin.id or ""))

try:
    fname = portin.loas.create("loa.pdf", {'content-type': 'application/pdf'})
except RestError as error:
    sys.exit(error)

print("LOA uploaded: " + (fname or ""))

try:
    res=portin.loas.update(fname,"loa.pdf",{'content-type':'application/pdf'})
except RestError as error:
    sys.exit(error)

print("LOA successfully updated")