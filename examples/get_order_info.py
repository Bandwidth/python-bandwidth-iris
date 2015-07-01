from iris_sdk.models.accounts import Account
from iris_sdk.client import Client

class GetOrderInfo():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)
        self._acc = Account(self._client)

        # Completed
        self._run("e2cbe50e-a23e-4bdc-b92b-00eff444ca17")
        # Failed
        self._run("15b6fa5f-da6e-47a3-8cb1-f2ee4ca36ea9")

    def _run(self, order_id):

        print("\n--- Order " + order_id + " ---\n")

        # Completed
        order = self._acc.orders.order(order_id)

        print("name: " + (order.details.name or ""))
        print("status: " + (order.order_status or ""))
        print("customer order: " + (order.details.customer_order_id or ""))
        print("site id: " + (order.details.site_id or ""))
        print("peer id: " + (order.details.peer_id or ""))
        print("created by: " + (order.created_by_user or ""))
        print("created: " + (order.details.order_created_date or ""))
        print("modified: " + (order.last_modified_date or ""))
        print("completed quantity: " + (order.completed_quantity or ""))
        print("pending quantity: " + (order.pending_quantity or ""))
        print("complete date: " + (order.order_complete_date or ""))
        print("failed: " + (order.failed_quantity or ""))
        print("back order requested: " + \
            (order.details.back_order_requested or ""))
        print("partial allowed: " + (order.details.partial_allowed or ""))

        print("completed numbers:")
        for number in order.completed:
            print("    " + (number or ""))

        print("search and order:")
        search_and_order = order.details.area_search
        print("    area code: " + (search_and_order.area_code or ""))
        print("    quantity: " + (search_and_order.quantity or ""))

        print("failed numbers:")
        for number in order.failed:
            print("    " + (number or ""))

        print("errors:")
        for error in order.errors:
            print("    code: " + (error.code or ""))
            print("        info: " + (error.description or ""))
            print("        tn: " + (error.telephone_number or ""))