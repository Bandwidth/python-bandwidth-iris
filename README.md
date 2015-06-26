# Python client library for IRIS / BBS API

## Needed tools

    - Python 2.7 or 3.x
    - pip

## Imports

    - future
    - mock (for py2)
    - requests

## Installation
```console
pip install iris_sdk
```

## Testing
```console
python -m unittest discover
```

## Examples

## Setup

```
from iris_sdk.account import Account
from iris_sdk.client import Client
```

```
client = Client(filename=<full_path>)
```
or
```
client = Client("http://foo.bar", 123456, "foo", "bar")
```

```
acc = Account(client)
```

### Accounts

```
acc.get()

print(acc.account_id)
print(acc.company_name)
print(acc.address.house_number)
print(acc.contact.first_name)
```

### Avalable numbers

```
numbers_list = acc.available_numbers.list({"areaCode": "435"})
```
or
```
numbers_list = acc.available_numbers_list({"areaCode": "435"})
```

```
for telephone_number in numbers_list:
    print(telephone_number)
```

### In-service numbers

```
numbers_list = acc.in_service_numbers.list({"areaCode": "435"})
```
or
```
numbers_list = acc.in_service_numbers_list({"areaCode": "435"})
```

```
for telephone_number in numbers_list:
    print(telephone_number)
```