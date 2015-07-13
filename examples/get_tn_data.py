from iris_sdk.models.tns import Tns
from iris_sdk.client import Client
from requests.exceptions import HTTPError

class GetTnData():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        tns = Tns(client=self._client)

        print("\n--- TN data ---\n")

        phone_number = tns.get(7576768750)
        site = phone_number.site.get()

        print("site:")
        print("    id: " + (site.id or ""))
        print("    name: " + (site.name or ""))

        sip_peer = phone_number.sip_peer.get()

        print("\nSIP peer:")
        print("    id: " + (sip_peer.id or ""))
        print("    name: " + (sip_peer.name or ""))

        rate_center = phone_number.tn_rate_center.get()

        print("\nrate center:")
        print("    state: " + (rate_center.state or ""))
        print("    name: " + (rate_center.name or ""))

        lca = phone_number.lca.get()

        print("\nLCA:")
        for npanxx in lca.listof_npanxx.items:
            print("    " + (npanxx or ""))

        print("LCA rate centers:")
        for center in lca.location.rate_centers.items:
            print("    state: " + (center.state or "center"))
            for rc in center.rcs.items:
                print("        " + (rc or ""))

        print("\nLata: " + (phone_number.tn_lata.get().lata or ""))

        history = phone_number.history.list()
            
        print("\nHistory:")
        for status in history.items:
            print("    account: " + (status.account_id or ""))
            print("    last modified: "+(status.last_modified_date or ""))
            print("    user: " + (status.user_id or ""))
            print("    order: " + (status.order_id or ""))
            print("    order created: " +(status.order_create_date or ""))
            print("    order type: " + (status.order_type or ""))
            print("    status: " + (status.status or ""))

        print("\nreservation:")
        try:
            reservation = phone_number.tnreservation.get()
        except HTTPError as error:
            print(error)