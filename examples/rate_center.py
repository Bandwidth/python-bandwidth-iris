import sys

from iris_sdk import Client, RateCenters, RestError

if len(sys.argv) < 2:
    sys.exit("usage: python rate_center.py [state], e.g.:\n" +
        "python rate_center.py NJ")

rate_centers = RateCenters(client=Client(filename="config.cfg"))

print("\n")

try:
    centers = rate_centers.list({"state": sys.argv[1]})
except RestError as error:
    sys.exit(error)

print("\ntotal for search: " + (rate_centers.total_count or ""))

for rc in centers.items:
    print((rc.abbreviation or "") + " (" + (rc.name or "") + ")")