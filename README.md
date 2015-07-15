# Python client library for IRIS / BBS API

## Needed tools

    - Python 2.7, or 3.3/3.4
    - pip

## Requires

    - future
    - mock (for py2)
    - requests

## Install
```console
pip install -e git+https://github.com/scottbarstow/iris-python#egg=iris_sdk
```

## Testing
```console
python -m unittest discover
```

## Usage

```python
from iris_sdk import Account, Client
```

```python
client = Client(url="http://foo.bar", account_id=123456, username="foo",
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
username   = foo
password   = bar

[rest]
url = http://foo.bar
```

## Examples

There is an 'examples' folder in the source tree that shows how each of the
API objects work with simple example code. To run the examples edit
'config.cfg' to match your IRIS credentials and run the examples individually,
e.g.,

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

Account has related entities such Orders, Sites, etc.

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
        in_service_numbers = acc.in_service_numbers.list(
            {"page": page, "size": 10})
    page = acc.in_service_numbers.links.next
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
rate_centers.list({"page": page, "size": 10})
```

### Disconnected numbers

```python
account.disconnected_numbers.list({"areaCode": 919})
```

### Disconnecting telephone numbers

The Disconnect object is used to disconnect numbers from an account.
Creates a disconnect order that can be tracked.

#### Creating disconnect orders

```python
disconnect = account.disconnects.add({
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
disconnect.notes.add({"user_id": "spam", "description": "ham"})
```

#### Getting all order's notes

```python
notes = disconnect.notes.list()
```

### Dlda

#### Creating orders

```python
dlda = account->dldas.add({
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
                    "address_yype": "AddressType"
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

### In-service numbers

```python
account.in_service_numbers.list({"areaCode": "919"})
```

### Lidb

#### Creating orders

```python
lidb = account.lidbs.add({
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