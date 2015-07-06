from iris_sdk.models.account import Account
from iris_sdk.client import Client

class Movetns():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- Moving SIP peers TNs ---\n")

        sites = acc.sites.list()

        site = sites.items[0]

        sip_peers = site.sip_peers.list()

        sip_peer = sip_peers.items[0]

        sip_peer.movetns.add(123456789)
        print("moving TNs for peer " +sip_peer.id +", site " +site.id +" ...")
        sip_peer.movetns.save()