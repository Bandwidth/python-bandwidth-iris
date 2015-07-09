from iris_sdk.models.account import Account
from iris_sdk.client import Client

class GetAccountHosts():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        hosts = acc.hosts.list()

        print("\n--- Account hosts ---\n")

        for site_host in hosts.items:
            print("site " + (site_host.id or ""))
            for sip_peer_host in site_host.sip_peer_hosts.items:
                print("    sip peer " + (sip_peer_host.id or ""))
                print("        sms:")
                for sms_host in sip_peer_host.sms_hosts.items:
                    print("            host name: " + \
                        (sms_host.host_name or ""))
                    print("            port: " + \
                        (sms_host.port or ""))
                print("        termination:")
                for term_host in sip_peer_host.termination_hosts.items:
                    print("            host name: " + \
                        (term_host.host_name or ""))
                    print("            port: " + (term_host.port or ""))
                print("        voice:")
                for voice_host in sip_peer_host.voice_hosts.items:
                    print("            host name: " + \
                        (voice_host.host_name or ""))
                    print("            port: " + (voice_host.port or ""))