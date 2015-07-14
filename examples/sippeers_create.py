import sys

from iris_sdk import Account, Client, RestError

if len(sys.argv) < 4:
    sys.exit("usage: python sippeer_create.py [host] [peer name] [site], " +
        "e.g.:\npython sippeer_create.py 92.168.181.95 peer12 2297")

acc = Account(client=Client(filename="config.cfg"))

print("\n")

host = sys.argv[1]
name = sys.argv[2]
site = sys.argv[3]

try:
    sip_peer = acc.sites.get(site).sip_peers.add({
        "peer_name": name,
        "is_default_peer": "true",
        "short_messaging_protocol": "SMPP",
        "voice_hosts": {
            "host": [{
                "host_name": host
            }]
        },
        "sms_hosts": {
            "host": [{
                "host_name": host
            }]
        },
        "termination_hosts": {
            "termination_host": [{
                "host_name": host,
                "port": "0",
                "customer_traffic_allowed": "DOMESTIC",
                "data_allowed": "true"
            }]
        }
    })
except RestError as error:
    sys.exit(error)

print("id: " + (sip_peer.id or ""))
print("name: " + (sip_peer.name or ""))
print("default peer: " + (sip_peer.is_default_peer))
print("sms protocol: " + (sip_peer.short_messaging_protocol or ""))
print("voice hosts:")
for host in sip_peer.voice_hosts.items:
    print("    " + (host.host_name or ""))
print("sms hosts:")
for host in sip_peer.sms_hosts.items:
    print("    " + (host.host_name or ""))
print("termination hosts:")
for host in sip_peer.termination_hosts.items:
    print("    " + (host.host_name or ""))
    print("        port: " + (host.port or ""))
    print("        data allowed: " +(host.data_allowed or ""))
    print("        customer traffic allowed: " +
        (host.customer_traffic_allowed or ""))