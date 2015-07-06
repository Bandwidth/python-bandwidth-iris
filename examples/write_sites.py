from iris_sdk.models.account import Account
from iris_sdk.client import Client

class WriteSites():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- Writing sites data ---\n")

        sites = acc.sites.list()

        site = sites.items[1]
        site.address.house_number = "123"
        site.address.street_name = "123"
        site.address.city = "123"
        site.address.state_code = "WA"
        site.address.zip_code = "aaa"
        site.address.address_type = "Service"

        print("saving " + site.id + " ...")
        site.save()
        print("ok")

        newsite = acc.sites.add()

        newsite.name = "foo"
        newsite.address.house_number = "12345"
        newsite.address.street_name = "12345"
        newsite.address.city = "12345"
        newsite.address.state_code = "WA"
        newsite.address.zip_code = "aaaaaaaaaaaaaa"
        newsite.address.address_type = "Service"

        print("adding new site ...")
        newsite.save()
        print("ok, id = " + newsite.id)

        newsite = acc.sites.get(newsite.id)

        print("deleting site " + newsite.id + " ...")
        newsite.delete()
        print("ok")