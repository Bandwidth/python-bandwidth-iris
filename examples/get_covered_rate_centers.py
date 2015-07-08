from iris_sdk.models.covered_rate_centers import CoveredRateCenters
from iris_sdk.client import Client

class GetCoveredRateCenters():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        rc = CoveredRateCenters(client=self._client)

        print("\n--- Covered rate Centers ---\n")

        rate_centers = rc.list({"page":1,"size":20})

        print("total for search: " + (rc.result_count or ""))

        for center in rate_centers.items:
            print(center.id or "")
            print("    name: " + (center.name or ""))
            print("    abbreviation: " + (center.abbreviation or ""))
            print("    state: " + (center.state or ""))
            print("    lata: " + (center.lata or ""))
            print("    tiers:")
            for tier in center.tiers.items:
                print("        " + (tier.tier or ""))

        center = rate_centers.items[0].get()
        print("\n" + (center.name or "") + " (" + (center.id or "") + ")")
        print("    available: " + (center.available_number_count or ""))
        print("    zip codes:")
        for zip in center.zip_codes.items:
            print("        " + (zip.zip_code or ""))
        print("    cities:")
        for city in center.cities.items:
            print("        " + (city.city or ""))
        print("    tiers:")
        for tier in center.tiers.items:
            print("        " + (tier.tier or ""))
        print("    NPA-NXX:")
        for npa in center.npa_nxx_xs.items:
            print("        " + (npa.npa_nxx_x or ""))
        print("    local rate centers:")
        for lrc in center.local_rate_centers.items:
            print("        " + (lrc.id or ""))