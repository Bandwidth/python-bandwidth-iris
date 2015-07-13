from iris_sdk.models.rate_centers import RateCenters
from iris_sdk.client import Client

class GetRateCenters():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        rc = RateCenters(client=self._client)

        print("\n--- Rate Centers ---\n")

        rate_centers = rc.list({"state": "NC"})

        print("total for search: " + (rc.total_count or ""))

        for center in rate_centers.items:
            print((center.abbreviation or "") +" (" +(center.name or "") +")")