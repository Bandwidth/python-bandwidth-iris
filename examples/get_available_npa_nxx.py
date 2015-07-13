from iris_sdk.client import Client
from iris_sdk.include.xml_consts import *
from iris_sdk.models.account import Account

class GetAvailableNpaNxx():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- Available NPA/NXX ---\n")

        available_npa = \
            acc.available_npa_nxx.list({"areaCode": "435"})

        for npa in available_npa.items:
            print(" - ")
            print("    city: " + (npa.city or ""))
            print("    NPA: " + (npa.npa or ""))
            print("    NXX: " + (npa.nxx or ""))
            print("    state: " + (npa.state or ""))
            print("    quantity: " + (npa.quantity or ""))