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

If an example take command line parameters, you will get the usage info by
just executing it.

"" API objects

""" General principles

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

""" Pagination

Some API objects provide paginated result sets and require the use of
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

""" Available numbers

```python
account.available_numbers.list({"areaCode": 818})
```

""" Available Npa-Nxx

```python
account.available_npa_nxx.list({"state": "NJ"})
```

""" Cities

```python
from iris_sdk import Cities

cities = Cities(client=client)
cities.list({"state": "NC"})
```

""" Covered rate centers