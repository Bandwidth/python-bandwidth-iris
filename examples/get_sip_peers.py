from iris_sdk.models.account import Account
from iris_sdk.client import Client

class GetSipPeers():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- SIP peers ---\n")

        site = acc.sites.get(2297)

        sip_peers = site.sip_peers.list()
        for sip_peer in sip_peers.items:
            print("Peer " + (sip_peer.id or "") + ":")
            print("    name: " + (sip_peer.name or ""))
            print("    default peer: " + (sip_peer.is_default_peer))
            print("    sms protocol: " + \
                (sip_peer.short_messaging_protocol or ""))
            print("    voice hosts:")
            for host in sip_peer.voice_hosts.items:
                print("        " + (host.host_name or ""))
            print("    sms hosts:")
            for host in sip_peer.sms_hosts.items:
                print("        " + (host.host_name or ""))
            print("    termination hosts:")
            for host in sip_peer.termination_hosts.items:
                print("        " + (host.host_name or ""))
                print("            port: " + (host.port or ""))
                print("            data allowed: " +(host.data_allowed or ""))
                print("            customer traffic allowed: " + \
                    (host.customer_traffic_allowed or ""))