from iris_sdk.models.cities import Cities
from iris_sdk.client import Client

class GetCities():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        cities = Cities(client=self._client)

        print("\n--- Cities ---\n")

        cities_list = cities.list({"state": "NC"})

        print("total for search: " + (cities.result_count or ""))

        for city in cities_list.items:
            print((city.rc_abbreviation or "") +" (" +(city.name or "") + ")")