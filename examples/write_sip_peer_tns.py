from iris_sdk.client import Client
from iris_sdk.models.account import Account

class WriteSipPeerTns():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- SIP peer TNs ---\n")

        sip_peer = acc.sites.get(2297).sip_peers.get(500709)
        tns = sip_peer.tns.list()

        phone = tns.items[-1]

        phone.rpid_format = "e164"
        print("saving " + (phone.full_number or "") + " ...")
        phone.save()
        print("ok")