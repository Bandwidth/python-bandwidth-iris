from iris_sdk.models.account import Account
from iris_sdk.client import Client

class WriteSipPeers():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- Getting peers list ---\n")

        sites = acc.sites.list()

        site = sites.items[0]

        sip_peers = site.sip_peers.list()

        sip_peer = sip_peers.items[0]

        sip_peer.address.house_number = "1"
        sip_peer.address.street_name = "street"
        sip_peer.address.city = "123"
        sip_peer.address.state_code = "WA"
        sip_peer.address.zip_code = "aaa"
        sip_peer.address.address_type = "Service"
        sip_peer.calling_name.display = "true"
        sip_peer.calling_name.enforced = "true"
        print("saving peer " + sip_peer.id + " for site " + site.id + " ...")
        sip_peer.save()
        print("ok")

        newpeer = site.sip_peers.add()

        newpeer.peer_name = "foo is not bar"
        newpeer.address.house_number = "1"
        newpeer.address.street_name = "street"
        newpeer.address.city = "123"
        newpeer.address.state_code = "WA"
        newpeer.address.zip_code = "aaa"
        newpeer.address.address_type = "Service"
        newpeer.calling_name.display = "true"
        newpeer.calling_name.enforced = "true"

        host = newpeer.termination_hosts.add()
        host.host_name = "192.31.31.73"

        print("adding new peer " + " for site " + site.id + " ...")
        newpeer.save()

        print("ok, id = " + newpeer.id)

        newpeer = site.sip_peers.get(newpeer.id)

        print("deleting peer " + newpeer.id + " for site " + site.id + " ...")
        newpeer.delete()
        print("ok")