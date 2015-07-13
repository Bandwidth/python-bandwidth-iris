import sys

from iris_sdk import Cities, Client

if len(sys.argv) < 2:
    sys.exit("usage: python cities.py [state], e.g.:\n python cities.py NJ")

cities = Cities(client=Client(filename="config.cfg"))

cities_list = cities.list({"state": sys.argv[1]})

print("\ntotal for search: " + (cities.result_count or ""))

for city in cities_list.items:
    print((city.rc_abbreviation or "") + " (" + (city.name or "") + ")")