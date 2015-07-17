#!/usr/bin/env python

import os
import sys

# For coverage.
if __package__ is None:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from unittest import main, TestCase

import requests
import requests_mock

from iris_sdk.client import Client
from iris_sdk.models.account import Account

XML_RESPONSE_SIP_PEER_GET = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<SipPeerResponse><SipPeer><PeerId>500651</PeerId>"
    b"<PeerName>Something</PeerName><IsDefaultPeer>false</IsDefaultPeer>"
    b"<ShortMessagingProtocol>SMPP</ShortMessagingProtocol></SipPeer>"
    b"</SipPeerResponse>"
)

XML_RESPONSE_SIP_PEER_TNS = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<SipPeerTelephoneNumbersResponse><SipPeerTelephoneNumbers>"
    b"<SipPeerTelephoneNumber><FullNumber>8183386251</FullNumber>"
    b"</SipPeerTelephoneNumber><SipPeerTelephoneNumber>"
    b"<FullNumber>8183386252</FullNumber></SipPeerTelephoneNumber>"
    b"</SipPeerTelephoneNumbers></SipPeerTelephoneNumbersResponse>"
)

XML_RESPONSE_SIP_PEER_TNS_TOTAL = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<SipPeerTelephoneNumbersCountResponse><SipPeerTelephoneNumbersCounts>"
    b"<SipPeerTelephoneNumbersCount>4</SipPeerTelephoneNumbersCount>"
    b"</SipPeerTelephoneNumbersCounts></SipPeerTelephoneNumbersCountResponse>"
)

XML_RESPONSE_SIP_PEERS_LIST = (
   b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
   b"<TNSipPeersResponse><SipPeers><SipPeer><PeerId>500709</PeerId>"
   b"<PeerName>Test4 Peer</PeerName><IsDefaultPeer>true</IsDefaultPeer>"
   b"<ShortMessagingProtocol>SMPP</ShortMessagingProtocol><VoiceHosts>"
   b"<Host><HostName>192.168.181.94</HostName></Host></VoiceHosts>"
   b"<VoiceHostGroups/><SmsHosts><Host><HostName>192.168.181.94</HostName>"
   b"</Host></SmsHosts><TerminationHosts><TerminationHost>"
   b"<HostName>192.168.181.94</HostName><Port>0</Port>"
   b"<CustomerTrafficAllowed>DOMESTIC</CustomerTrafficAllowed>"
   b"<DataAllowed>true</DataAllowed></TerminationHost></TerminationHosts>"
   b"</SipPeer></SipPeers></TNSipPeersResponse>"
)

class ClassSitesTest(TestCase):

    """Test sites"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)
        cls._site = cls._account.sites.create({"id": "1337"}, False)
        cls._sip_peers = cls._site.sip_peers

    @classmethod
    def tearDownClass(cls):
        del cls._sip_peers
        del cls._site
        del cls._account
        del cls._client

    def test_get_tns(self):

        peer = self._sip_peers.create({"peer_id": "2489"}, False)
        tns = peer.tns

        with requests_mock.Mocker() as m:

            url = self._client.config.url + tns.get_xpath()
            m.get(url, content=XML_RESPONSE_SIP_PEER_TNS)

            phones = tns.list()

            self.assertEqual(len(phones.items), 2)
            self.assertEqual(phones.items[0].full_number, "8183386251")

    def test_movetns(self):

        peer = self._sip_peers.create({"peer_id": "2489"}, False)
        movetns = peer.movetns

        with requests_mock.Mocker() as m:

            url = self._client.config.url + movetns.get_xpath()
            m.post(url)

            movetns.add("123")
            movetns.add("456")

            movetns()

    def test_peer_create(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._sip_peers.get_xpath()
            m.post(url, headers={"location": ".../9999"})

            peer = self._sip_peers.create({
                "peer_name": "foo",
                "is_default_peer": "true",
                "short_messaging_protocol": "SMPP",
                "voice_hosts": {
                    "host": [{
                        "host_name": "192.168.181.90"
                    }]
                },
                "sms_hosts": {
                    "host": [{
                        "host_name": "192.168.181.90"
                    }]
                },
                "termination_hosts": {
                    "termination_host": [{
                        "host_name": "192.168.181.90",
                        "port": "0",
                        "customer_traffic_allowed": "DOMESTIC",
                        "data_allowed": "true"
                    }]
                }
            })

        self.assertEqual(peer.id, "9999")

    def test_peer_get(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._sip_peers.get_xpath() +\
                "/500651"
            m.get(url, content=XML_RESPONSE_SIP_PEER_GET)

            peer = self._sip_peers.get("500651")

            self.assertEqual(peer.id, "500651")
            self.assertEqual(peer.name, "Something")

    def test_peers_list(self):

        with requests_mock.Mocker() as m:

            url = self._client.config.url + self._sip_peers.get_xpath()
            m.get(url, content=XML_RESPONSE_SIP_PEERS_LIST)

            peers = self._sip_peers.list()

            self.assertEqual(len(peers.items), 1)
            self.assertEqual(peers.items[0].id, "500709")

    def test_tn_options(self):

        peer = self._sip_peers.create({"peer_id": "2489"}, False)
        tn = peer.tns.create({"full_number": "8183386251"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + tn.get_xpath()
            m.put(url)

            tn.call_forward = "9194394706"
            tn.rpid_format = "e164"
            tn.save()

    def test_totaltns(self):

        peer = self._sip_peers.create({"peer_id": "2489"}, False)

        with requests_mock.Mocker() as m:

            url = self._client.config.url + peer.totaltns.get_xpath()
            m.get(url, content=XML_RESPONSE_SIP_PEER_TNS_TOTAL)

            count = peer.totaltns.get().count

            self.assertEqual(count, "4")

if __name__ == "__main__":
    main()