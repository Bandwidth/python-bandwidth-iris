from iris_sdk.client import Client
from iris_sdk.models.account import Account

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

        site = sites.items[-1]
        totaltns = site.totaltns.get().count
        print("Site " + (site.id or "") + ", total TNs: " + (totaltns or ""))