# Python client library for IRIS / BBS API

## Needed tools

    - Python 3.5
    - pip

## Requires

    - future
    - requests

## Install
```console
pip install -e git+https://github.com/bandwidthcom/python-bandwidth-iris#egg=iris_sdk
```

## Testing

Tests require the *mock* and *requests_mock* packages. You can install them
with

```console
pip install -r requirements.txt
```
The tests can be run by issuing
```console
python -m unittest discover
```

## Usage

```python
from iris_sdk import Account, Client
```

```python
client = Client(url="https://dashboard.bandwidth.com/api", account_id=123456, username="foo",
    password="bar")
```
or
```python
client = Client(filename=<path to config>)
```

### Config format
```ini
[account]
account_id = 123456789
username   = spam
password   = ham

[rest]
url = https://dashboard.bandwidth.com/api
```

## Examples

There is an 'examples' folder in the source tree that shows how each of the
API objects work with simple example code. To run these make a copy of
'config.cfg.example', rename to 'config.cfg', edit it to match your IRIS
credentials and run the examples individually, e.g.,

```console
python available_numbers.py
```

If an example takes command line parameters, you will get the usage info by
just executing it.

## API objects

### General principles

In most cases you should use an Account object as a starting point.

```python
account = Account(client=client)
```

Account has related entities such as Orders, Sites, etc.

```python
sites = account.sites.list()
for site in sites.items:
   pass
```

### Pagination

Some resources provide paginated result sets and require the use of
page/size parameters. In these cases a Links object will be provided for
iterating over the results.

```python
in_service_numbers = account.in_service_numbers.list({"page": 1, "size": 10})

total = int(account.in_service_numbers.total_count)
total_displayed = len(in_service_numbers.items)
page = None

while total_displayed <= total:
    if page is not None:
        in_service_numbers = account.in_service_numbers.list(
            {"page": page, "size": 10})
    page = account.in_service_numbers.links.next
    for phone_number in in_service_numbers.items:
        print(phone_number)
    total_displayed += len(in_service_numbers.items)
```

### Available numbers

```python
account.available_numbers.list({"areaCode": 818})
```

### Available Npa-Nxx

```python
account.available_npa_nxx.list({"state": "NJ"})
```

### Cities

```python
from iris_sdk import Cities

cities = Cities(client=client)
cities.list({"state": "NC"})
```

### Covered rate centers

```python
from iris_sdk import CoveredRateCenters

rate_centers = CoveredRateCenters(client=client)
rate_centers.list({"page": 1, "size": 10})
```

### Disconnected numbers

```python
account.disconnected_numbers.list({"areaCode": 919})
```

### Disconnecting telephone numbers

#### Creating disconnect orders

```python
disconnect = account.disconnects.create({
    "name": "test disconnect order 4",
    "customer_order_id": "Disconnect1234",
    "disconnect_telephone_number_order_type": {
        "telephone_number_list": {
            "telephone_number": ["9192755378", "9192755703"]
        }
    }
})
```

#### Getting order data

```python
disconnect = account.disconnects.get("b902dee1-0585-4258-becd-5c7e51ccf5e1")
```

#### Adding notes

```python
disconnect.notes.create({"user_id": "spam", "description": "ham"})
```

#### Getting all order's notes

```python
notes = disconnect.notes.list()
```

### Dlda

#### Creating orders

```python
dlda = account.dldas.create({
    "customer_order_id": "123",
    "dlda_tn_groups": {
        "dlda_tn_group": [{
            "telephone_numbers": {
                "telephone_number": ["4352154856"]
                "account_type": "RESIDENTIAL",
                "listing_type": "LISTED",
                "list_address": "true",
                "listing_name": {
                    "first_name": "FirstName",
                    "first_name2": "FirstName2",
                    "last_name": "LastName",
                    "designation": "Designation",
                    "title_of_lineage": "TitleOfLineage",
                    "title_of_address": "TitleOfAddress",
                    "title_of_address2": "TitleOfAddress2",
                    "title_of_lineage_name2": "TitleOfLineageName2",
                    "title_of_address_name2": "TitleOfAddressName2",
                    "title_of_address2_name2": "TitleOfAddress2Name2",
                    "place_listing_as": "PlaceListingAs",
                },
                "address": {
                    "house_prefix": "HousePrefix",
                    "house_number": "915",
                    "house_suffix": "HouseSuffix",
                    "pre_directional": "PreDirectional",
                    "street_name": "StreetName",
                    "street_suffix": "StreetSuffix",
                    "post_directional": "PostDirectional",
                    "address_line2": "AddressLine2",
                    "city": "City",
                    "state_code": "StateCode",
                    "zip": "Zip",
                    "plus_four": "PlusFour",
                    "country": "Country",
                    "address_type": "AddressType"
                }
            }
        }]
    }
})
```

#### Getting order data

```python
dlda = account.dldas.get("7802373f-4f52-4387-bdd1-c5b74833d6e2")
```

#### Retrieving dlda history

```python
dlda.history.list()
```

#### Getting a list of dldas

```python
account.dldas.list({"telephoneNumber": "9195551212"})
```

### Import TN Checker
```python
# returns an array of portable TN's
result = account.import_tn_checker(numbers=["3032281000", "9195551234"])
print(result)    # ['3032281000', '9195551234']
```

### In-service numbers

```python
account.in_service_numbers.list({"areaCode": "919"})
```

### Lidb

#### Creating orders

```python
lidb = account.lidbs.create({
    "lidb_tn_groups": {
        "lidb_tn_group": [{
            "telephone_numbers": {
                "telephone_number": ["4352154856"]
            },
            "subscriber_information": "Steve",
            "use_type": "RESIDENTIAL",
            "visibility": "PUBLIC"
        },
        {
            "telephone_numbers": {
                "telephone_number": ["4352154855"]
            },
            "subscriber_information": "Steve",
            "use_type": "RESIDENTIAL",
            "visibility": "PUBLIC"
        }]
    }
})

```

#### Getting order data

```python
lidb = account.lidbs.get("7802373f-4f52-4387-bdd1-c5b74833d6e2")
```

#### Getting a list of lidbs

```python
lidbs = account.lidbs.list({"last_modified_after": "mm-dd-yy",
    "telephone_number": "888"})
```

### LNP Checker

```python
account.lnpChecker(["4109255199", "9196190594"], "true")
```

### Phone numbers orders

#### Creating orders

```python
order = account.orders.create({
    "name": "Available Telephone Number order",
    "site_id": "2297",
    "customer_order_id": "123456789",
    "existing_telephone_number_order_type": {
        "telephone_number_list": {
            "telephone_number": ["9193752369", "9193752720", "9193752648"]
        }
    }
})
```

#### Getting order data

```python
response = account.orders.get("f30a31a1-1de4-4939-b094-4521bbe5c8df")
order = response.order
```

#### Getting a list of orders

```python
orders = account.orders.list()
```

#### Adding notes

```python
order.notes.create({"user_id": "spam", "description": "Test Note"})
```

#### Getting order's telephone numbers

```python
order.tns.list()
```

### Port-ins

#### Creating orders

```python
portin = account.portins.create({
    "billing_telephone_number": "6882015002",
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
        "phone_number": ["9882015025", "9882015026"]
    },
    "site_id": "365",
    "triggered": "false"
})
```

#### Getting order data

```python
portin = account.portinsget("d28b36f7-fa96-49eb-9556-a40fca49f7c6")
```

#### Getting a list of orders

```python
portins = account.portins.list({"pon": "a pon"})
```

#### Port-in instance methods and properties

```python
portin.save()
portin.delete()
portin.activation_status

status = portin.activation_status
status.auto_activation_date = "2014-08-30T18:30:00+03:00"
status.save()

portin.history
portin.totals
portin.notes
```

#### Port-in file management

```python
portin.loas.list({"metadata": "true"})
fname = portin.loas.create("loa.pdf", {'content-type': 'application/pdf'})
portin.loas.update(fname, "loa.pdf", {'content-type':'application/pdf'})
portin.loas.delete(fname)
portin.loas.metadata.get(fname)
portin.loas.metadata.document_name = "text.txt"
portin.loas.metadata.document_type = "invoice"
portin.loas.metadata.save()
portin.loas.metadata.delete()
```

### Rate Centers

```python
from iris_sdk import RateCenters
rc = RateCenters(client=client)
centers = rc.list({"state": "CA", "available": "true"})
```

### SIP Peers

#### Creating a SIP peer

```python
sip_peer = account.sites.list().items[0].sip_peers.create({
        "peer_name": name,
        "is_default_peer": "true",
        "short_messaging_protocol": "SMPP",
        "voice_hosts": {
            "host": [{
                "host_name": "92.168.181.95"
            }]
        },
        "sms_hosts": {
            "host": [{
                "host_name": "92.168.181.95"
            }]
        },
        "termination_hosts": {
            "termination_host": [{
                "host_name": "92.168.181.95",
                "port": "0",
                "customer_traffic_allowed": "DOMESTIC",
                "data_allowed": "true"
            }]
        }
    })
```

#### Getting a peer

```python
sip_peer = account.sites.list().items[0].sip_peers.get("500651")
```

#### Getting a list of SIP peers

```python
sip_peers = account.sites.list().items[0].sip_peers.list()
```

#### Deleting SIP peers

```python
sip_peer.delete()
```

#### Moving telephone numbers

```python
sip_peer.movetns.add("9192000046")
sip_peer.movetns()
```

#### Getting peer telephone numbers

```python
tns = sip_peer.tns.list()
```

#### Getting a single phone number

```python
tn = sip_peer.tns.get("8183386251")
```

#### Getting total number of numbers for a SIP peer

```python
count = sip_peer.totaltns.get()
```

#### Setting telephone number options

```python
tn = sip_peer.tns.get("8183386251")
tn.rpid_format = "e164"
tn.save()
```

### Sites

#### Creating a site

```python
site = acc.sites.create({
    "name": "test123456",
    "address": {
        "city": "Raleigh",
        "address_type": "Service",
        "house_number": "1",
        "street_name": "Avenue",
        "state_code": "NC",
        "zip": "27606"
    }
})
```

#### Updating a site

```python
site.name = "New Name"
site.save()
```

#### Deleting a site

```python
site.delete()
```

#### Getting a list of sites

```python
sites = account.sites.list()
```

#### Getting a list of site orders

```python
site.orders.list({"status": "disabled"})
```

#### Getting the total number of telephone numbers for a site

```python
site.totaltns.get()
```

#### Getting a list of site's port-in orders

```python
site.portins.list({"status": "disabled"})
```

### Subscriptions

#### Creating subscriptions

```python
subscription = account.subscriptions.create({
    "order_type": "portins",
    "order_id": "98939562-90b0-40e9-8335-5526432d9741",
    "email_subscription": {
        "email": "test@test.com",
        "digest_requested": "DAILY"
    }
})
```

#### Getting subscription information

```python
subscription = account.subscriptions.get(id)
```

#### Getting a list of subscriptions

```python
account.subscriptions.list({"orderType": "portins"})
```

#### Updating a subscription

```python
subscription.order_type = "portins"
subscription.save()
```

#### Deleting a subscription

```python
subscription.delete()
```

### TNs

#### Getting a phone number

```python
from iris_sdk import Tns

tns = Tns(client=client)
tn = tns.get(id)
```

#### Getting a list of TNs

```python
tns.list({"page": 1, "size": 10 })
```

#### Telephone number instance methods and properties

```python
tn = tns.get("7576768750")
site = tn.site.get()
sip_peer = tn.sip_peer.get()
tnreservation = tn.tnreservation
tn.tndetails.get()
rc = tn.tn_rate_center.get()
lata = tn.tn_lata.get()
lca = tn.lca.get()
history = tn.history.list()
```

### Reserving phone numbers

#### Create a reservation

```python
account.tnreservation.reserved_tn = "2512027430"
account.tnreservation.save()
```

#### Getting reservation info

```python
reservation = account.tnreservation.get("0099ff73-da96-4303-8a0a-00ff316c07aa")
```

#### Deleting a reservation

```python
reservation.delete()
```

### Get TN Option Orders
```python
orders = account.tn_option_orders.list()
print(orders.total_count)
print(orders.tn_option_order_summary.items[0].account_id)
```

### Get TN Option Order
```python
order = account.tn_option_orders.get("order_id")
print(order.order_create_date)
```

### Get TN Option Order (error)
```python
order = account.tn_option_orders.get("order_id_with_error")
print(order.error_list.error.items[0].description)
```

### Create PortOut Passcode
```python
order = account.tn_option_orders.create({
    "customer_order_id": "custom order",
    "tn_option_groups": {
        "tn_option_group": [
            {
                "port_out_passcode": "12abd38",
                "telephone_numbers": {
                    "telephone_number": [
                        "2018551020"
                    ]
                }
            }
        ]
    }
})

print(order.order_create_date)
```

### Create Call Forward Number
```python
order = account.tn_option_orders.create({
    "customer_order_id": "custom order",
    "tn_option_groups": {
        "tn_option_group": [
            {
                "call_forward": "2018551022",
                "telephone_numbers": {
                    "telephone_number": [
                        "2018551020"
                    ]
                }
            }
        ]
    }
})

print(order.order_create_date)
```

### Enable SMS
```python
order = account.tn_option_orders.create({
    "customer_order_id": "custom order",
    "tn_option_groups": {
        "tn_option_group": [
            {
                "sms": "on",
                "telephone_numbers": {
                    "telephone_number": [
                        "2018551020"
                    ]
                }
            }
        ]
    }
})

print(order.order_create_date)
```
