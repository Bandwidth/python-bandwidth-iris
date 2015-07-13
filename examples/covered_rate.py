import sys

from iris_sdk import Client, CoveredRateCenters, RestError

if len(sys.argv) < 2:
    sys.exit("usage: python covered_rate.py [zip], e.g.:" +
        "\npython covered_rate.py 27609")

rate_centers = CoveredRateCenters(client=Client(filename="config.cfg"))

print("\n")

try:
    rc = rate_centers.list({"zip": sys.argv[1], "page": 1, "size": 30})
except RestError as error:
    sys.exit(error)

print("total for search: " + (rate_centers.total_count or ""))

for center in rc.items:
    print(center.id or "")
    print("    name: " + (center.name or ""))
    print("    abbreviation: " + (center.abbreviation or ""))
    print("    state: " + (center.state or ""))
    print("    lata: " + (center.lata or ""))
    print("    tiers:")
    for tier in center.tiers.items:
        print("        " + (tier or ""))