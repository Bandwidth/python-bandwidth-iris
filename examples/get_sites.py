from iris_sdk.models.account import Account
from iris_sdk.client import Client

class GetSites():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- Sites ---\n")

        sites = acc.sites.list()

        for site in sites.items:
            print("id: " + (site.id or ""))
            print("    name: " + (site.name or ""))
            print("    description: " + (site.description or ""))