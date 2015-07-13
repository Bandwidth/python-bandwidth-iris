import sys

from iris_sdk import Cities, Client, RestError

if len(sys.argv) < 2:
    sys.exit("usage: python cities.py [state], e.g.:\n python cities.py NJ")

cities = Cities(client=Client(filename="config.cfg"))

print("\n")

try:
    cities_list = cities.list({"state": sys.argv[1]})
except RestError as error:
    sys.exit(error)

print("\ntotal for search: " + (cities.result_count or ""))

for city in cities_list.items:
    print((city.rc_abbreviation or "") + " (" + (city.name or "") + ")")