from iris_sdk.models.accounts import Account
from iris_sdk.client import Client

class GetOrdersExample():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(self._client)

        print("\n--- Orders ---\n")

        orders = acc.orders.list({"page": 1, "size": 20})

        total_displayed = len(orders)
        total = int(acc.orders.search_count)

        print("total for search: " + acc.orders.search_count)

        page = None
        while (total_displayed <= total):

            if (page is not None):
                orders = acc.orders.list({"page": page, "size": 20})

            page = acc.orders.links.next

            for order in orders:

                print(order.order_id)
                print("    status: " + order.order_status)

                print("    states:")
                for state in order.telephone_number_details.states.items:
                    print("        state: " + (state.name or ""))
                    print("            phone numbers: " + (state.count or ""))

                print("    rate centers:")
                for rate_center in order.telephone_number_details.\
                        rate_centers.items:
                    print("        rate center: " + (rate_center.name or ""))
                    print("            phone numbers: " +\
                        (rate_center.count or ""))

                print("    cities:")
                for city in order.telephone_number_details.cities.items:
                    print("        city: " + (city.name or ""))
                    print("            phone numbers: " + (city.count or ""))

                print("    tiers:")
                for tier in order.telephone_number_details.tiers.items:
                    print("        tier: " + (tier.name or ""))
                    print("            phone numbers: " + (tier.count or ""))

                print("    vendors:")
                for vendor in order.telephone_number_details.vendors.items:
                    print("        vendor id: " + (vendor.id or ""))
                    print("            vendor name: " + (vendor.name or ""))
                    print("            phone numbers: " +(vendor.count or ""))

            total_displayed += len(orders)