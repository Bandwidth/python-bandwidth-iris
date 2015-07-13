from iris_sdk.client import Client
from iris_sdk.models.account import Account

class GetSipPeerTns():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- SIP peer TNs ---\n")

        sip_peer = acc.sites.get(2297).sip_peers.get(500709)
        tns = sip_peer.tns.list()

        phone = tns.items[-1]
        print(phone.full_number or "")
        print("    call forward: " + (phone.call_forward or ""))
        print("    display: " + (phone.calling_name_display or ""))
        print("    attributes: ")
        for attribute in phone.tn_attributes.items:
            print(attribute or "")

        total = sip_peer.totaltns.get().count
        print("SIP peer " +(sip_peer.id or "") +", total TNs: "+(total or ""))

        phone.rpid_format = "e164"
        phone.save()