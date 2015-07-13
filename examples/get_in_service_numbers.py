from iris_sdk.client import Client
from iris_sdk.include.xml_consts import *
from iris_sdk.models.account import Account

class GetInServiceNumbers():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- In-service numbers ---\n")

        in_service_numbers = acc.in_service_numbers.list(
            {XML_PARAM_PAGE: 1, XML_PARAM_SIZE: 20})

        print("Totals for search: " + \
            (acc.in_service_numbers.total_count or ""))

        for phone_number in in_service_numbers.items:
            print(phone_number)

        print("Numbers in service: " + \
            (acc.in_service_numbers.totals.get().count or ""))