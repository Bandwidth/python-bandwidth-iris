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
from iris_sdk.utils.rest import RestError

XML_RESPONSE_ACCOUNT_GET = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b" <AccountResponse>"
    b"    <Account>"
    b"        <AccountId>123456</AccountId>"
    b"        <CompanyName>Spam</CompanyName>"
    b"        <AccountType>Ham</AccountType>"
    b"        <Tiers>"
    b"            <Tier>0</Tier>"
    b"        </Tiers>"
    b"        <Address>"
    b"            <HouseNumber>900</HouseNumber>"
    b"        </Address>"
    b"        <Contact>"
    b"            <FirstName>Eggs</FirstName>"
    b"        </Contact>"
    b"    </Account>"
    b"</AccountResponse>"
)

XML_RESPONSE_AVAILABLE_NPA_NXX_GET = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<SearchResultForAvailableNpaNxx>"
    b"    <AvailableNpaNxxList>"
    b"        <AvailableNpaNxx>"
    b"            <City>COMPTON:COMPTON DA</City>"
    b"            <Npa>424</Npa>"
    b"            <Nxx>242</Nxx>"
    b"            <Quantity>7</Quantity>"
    b"            <State>CA</State>"
    b"        </AvailableNpaNxx>"
    b"        <AvailableNpaNxx>"
    b"            <City>COMPTON:GARDENA DA</City>"
    b"            <Npa>424</Npa>"
    b"            <Nxx>246</Nxx>"
    b"            <Quantity>5</Quantity>"
    b"            <State>CA</State>"
    b"        </AvailableNpaNxx>"
    b"    </AvailableNpaNxxList>"
    b"</SearchResultForAvailableNpaNxx>"
)

XML_RESPONSE_AVAILABLE_NUMBERS_GET = (
    b"<SearchResult>"
    b"    <ResultCount>3</ResultCount>"
    b"    <TelephoneNumberList>"
    b"        <TelephoneNumber>6093252507</TelephoneNumber>"
    b"        <TelephoneNumber>6093570994</TelephoneNumber>"
    b"        <TelephoneNumber>6093574598</TelephoneNumber>"
    b"    </TelephoneNumberList>"
    b"</SearchResult>"
)

XML_RESPONSE_AVAILABLE_NUMBERS_DETAIL_GET = (
    b"<SearchResult>"
    b"    <ResultCount>3</ResultCount>"
    b"    <TelephoneNumberDetailList>"
    b"        <TelephoneNumberDetail>"
    b"            <City>ALLENTOWN</City>"
    b"            <LATA>222</LATA>"
    b"            <RateCenter>ALLENTOWN </RateCenter>"
    b"            <State>NJ</State>"
    b"            <FullNumber>6093252507</FullNumber>"
    b"            <Tier>0</Tier>"
    b"            <VendorId>49</VendorId>"
    b"            <VendorName>Bandwidth CLEC</VendorName>"
    b"        </TelephoneNumberDetail>"
    b"        <TelephoneNumberDetail>"
    b"            <City>ALLENTOWN</City>"
    b"            <LATA>222</LATA>"
    b"            <RateCenter>ALLENTOWN </RateCenter>"
    b"            <State>NJ</State>"
    b"            <FullNumber>6093570994</FullNumber>"
    b"            <Tier>0</Tier>"
    b"            <VendorId>49</VendorId>"
    b"            <VendorName>Bandwidth CLEC</VendorName>"
    b"        </TelephoneNumberDetail>"
    b"        <TelephoneNumberDetail>"
    b"            <City>ALLENTOWN</City>"
    b"            <LATA>222</LATA>"
    b"            <RateCenter>ALLENTOWN </RateCenter>"
    b"            <State>NJ</State>"
    b"            <FullNumber>6093574598</FullNumber>"
    b"            <Tier>0</Tier>"
    b"            <VendorId>49</VendorId>"
    b"            <VendorName>Bandwidth CLEC</VendorName>"
    b"        </TelephoneNumberDetail>"
    b"    </TelephoneNumberDetailList>"
    b"</SearchResult>"
)

XML_RESPONSE_AVAILABLE_NUMBERS_ERROR = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<SearchResult>"
    b"    <Error>"
    b"        <Code>4010</Code>"
    b"        <Description>Unable to perform search.</Description>"
    b"    </Error>"
    b"</SearchResult>"
)

XML_RESPONSE_DISCONNECTED_NUMBERS_GET = (
    b"<?xml version=\"1.0\"?>"
    b"<TNs>"
    b"    <TotalCount>4</TotalCount>"
    b"    <Links>"
    b"        <first></first>"
    b"    </Links>"
    b"    <TelephoneNumbers>"
    b"        <Count>2</Count>"
    b"        <TelephoneNumber>4158714245</TelephoneNumber>"
    b"        <TelephoneNumber>4352154439</TelephoneNumber>"
    b"    </TelephoneNumbers>"
    b"</TNs>"
)

XML_RESPONSE_LINE_OPTION_ORDER = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    b"<LineOptionOrderResponse>"
    b"    <LineOptions>"
    b"        <CompletedNumbers>"
    b"            <TelephoneNumber>2013223685</TelephoneNumber>"
    b"        </CompletedNumbers>"
    b"        <Errors>"
    b"            <Error>"
    b"                <TelephoneNumber>5209072452</TelephoneNumber>"
    b"                <ErrorCode>5071</ErrorCode>"
    b"                <Description>"
    b"                    Telephone number not available."
    b"                </Description>"
    b"            </Error>"
    b"            <Error>"
    b"                <TelephoneNumber>5209072451</TelephoneNumber>"
    b"                <ErrorCode>13518</ErrorCode>"
    b"                <Description>"
    b"                    CNAM for telephone number is applied at the "
    b"                    Location level and it is notapplicable at the TN "
    b"                    level."
    b"                </Description>"
    b"            </Error>"
    b"        </Errors>"
    b"    </LineOptions>"
    b"</LineOptionOrderResponse>"
)

XML_RESPONSE_LNP_CHECKER = (
    b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    b"<NumberPortabilityResponse>"
    b"    <SupportedRateCenters />"
    b"    <UnsupportedRateCenters>"
    b"        <RateCenterGroup>"
    b"            <RateCenter>BALTIMORE</RateCenter>"
    b"            <City>BALTIMORE</City>"
    b"            <State>MD</State>"
    b"            <LATA>238</LATA>"
    b"            <TnList>"
    b"                <Tn>4109255199</Tn>"
    b"                <Tn>4104685864</Tn>"
    b"            </TnList>"
    b"        </RateCenterGroup>"
    b"        <RateCenterGroup>"
    b"            <RateCenter>SPARKSGLNC</RateCenter>"
    b"            <City>SPARKS GLENCOE</City>"
    b"            <State>MD</State>"
    b"            <LATA>238</LATA>"
    b"            <TnList>"
    b"                <Tn>4103431313</Tn>"
    b"                <Tn>4103431561</Tn>"
    b"            </TnList>"
    b"        </RateCenterGroup>"
    b"    </UnsupportedRateCenters>"
    b"</NumberPortabilityResponse>"
)

XML_RESPONSE_TN_RESERVATION_GET = (
    b"<?xml version=\"1.0\"?>"
    b"<ReservationResponse>"
    b"    <Reservation>"
    b"        <ReservationId>0099ff73-da96-4303</ReservationId>"
    b"        <AccountId>14</AccountId>"
    b"        <ReservationExpires>0</ReservationExpires>"
    b"        <ReservedTn>2512027430</ReservedTn>"
    b"    </Reservation>"
    b"</ReservationResponse>"
)

XML_RESPONSE_TOTALS = (
    b"<Quantity>"
    b"    <Count>4</Count>"
    b"</Quantity>"
)

class ClassAccountTest(TestCase):

    """Test account mapping and resources"""

    @classmethod
    def setUpClass(cls):
        cls._client = Client("http://foo", "bar", "bar", "qux")
        cls._account = Account(client=cls._client)

    @classmethod
    def tearDownClass(cls):
        del cls._client
        del cls._account

    def test_account_get(self):
        self.assertEquals(self._account.id, "bar")
        self.assertEquals(self._account.get_xpath(),
            self._account._xpath.format(self._account.id))
        with requests_mock.Mocker() as m:
            m.get(self._account.client.config.url + self._account.get_xpath(),
                content=XML_RESPONSE_ACCOUNT_GET)
            self._account.get()
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(self._account.id, "123456")
            self.assertEquals(self._account.company_name, "Spam")
            self.assertEquals(self._account.account_type, "Ham")
            self.assertEquals(self._account.tiers.tier.items, ["0"])
            self.assertEquals(self._account.address.house_number, "900")
            self.assertEquals(self._account.contact.first_name, "Eggs")

    def test_available_numbers(self):
        self.assertEquals(self._account.available_numbers.get_xpath(),
            self._account.get_xpath() +
            self._account.available_numbers._xpath)
        with requests_mock.Mocker() as m:
            m.get(self._account.client.config.url+
                    self._account.available_numbers.get_xpath(),
                content=XML_RESPONSE_AVAILABLE_NUMBERS_GET)
            avail_numbers = self._account.available_numbers.list(
                {"state": "NJ"})
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(avail_numbers.items,
                ["6093252507", "6093570994", "6093574598"])
            self.assertEquals(self._account.available_numbers.result_count,
                "3")

    def test_available_numbers_detail(self):
        self.assertEquals(self._account.available_numbers.get_xpath(),
            self._account.get_xpath() +
            self._account.available_numbers._xpath)
        with requests_mock.Mocker() as m:
            m.get(self._account.client.config.url+
                    self._account.available_numbers.get_xpath(),
                content=XML_RESPONSE_AVAILABLE_NUMBERS_DETAIL_GET)
            avail_numbers = self._account.available_numbers.list(
                {"enableTNDetail": "true", "state": "NJ"})
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(avail_numbers.items[0].city, "ALLENTOWN")
            self.assertEquals(avail_numbers.items[0].lata, "222")
            self.assertEquals(avail_numbers.items[1].full_number,"6093570994")
            self.assertEquals(avail_numbers.items[1].tier, "0")
            self.assertEquals(avail_numbers.items[2].vendor_id, "49")
            self.assertEquals(avail_numbers.items[2].vendor_name,
                "Bandwidth CLEC")
            self.assertEquals(self._account.available_numbers.result_count,
                "3")

    def test_available_numbers_error(self):
        self.assertEquals(self._account.available_numbers.get_xpath(),
            self._account.get_xpath() +
            self._account.available_numbers._xpath)
        with requests_mock.Mocker() as m:
            m.get(self._account.client.config.url+
                    self._account.available_numbers.get_xpath(),
                content=XML_RESPONSE_AVAILABLE_NUMBERS_ERROR, status_code=400)
            with self.assertRaises(RestError):
                self._account.available_numbers.list(None)

    def test_disc_numbers(self):
        self.assertEquals(self._account.disconnected_numbers.get_xpath(),
            self._account.get_xpath() +
            self._account.disconnected_numbers._xpath)
        with requests_mock.Mocker() as m:
            m.get(self._account.client.config.url+
                    self._account.disconnected_numbers.get_xpath(),
                content=XML_RESPONSE_DISCONNECTED_NUMBERS_GET)
            disc_numbers = self._account.disconnected_numbers.list(
                {"page": 1, "type": "x"})
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(disc_numbers.items, ["4158714245","4352154439"])

    def test_disc_numbers_totals(self):
        self.assertEquals(
            self._account.disconnected_numbers.totals.get_xpath(),
                self._account.get_xpath() +
                self._account.disconnected_numbers._xpath +
                self._account.disconnected_numbers.totals._xpath
        )
        with requests_mock.Mocker() as m:
            m.get(self._account.client.config.url+
                    self._account.disconnected_numbers.totals.get_xpath(),
                content=XML_RESPONSE_TOTALS)
            count = self._account.disconnected_numbers.totals.get().count
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(count, "4")

    def test_in_service_numbers(self):
        self.assertEquals(self._account.in_service_numbers.get_xpath(),
            self._account.get_xpath() +
            self._account.in_service_numbers._xpath)
        with requests_mock.Mocker() as m:
            m.get(self._account.client.config.url+
                    self._account.in_service_numbers.get_xpath(),
                content=XML_RESPONSE_DISCONNECTED_NUMBERS_GET)
            numbers = self._account.in_service_numbers.list({"state": "NJ"})
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(numbers.items,["4158714245","4352154439"])
            self.assertEquals(self._account.in_service_numbers.total_count,
                "4")

    def test_in_service_numbers_totals(self):
        self.assertEquals(
            self._account.in_service_numbers.totals.get_xpath(),
                self._account.get_xpath() +
                self._account.in_service_numbers._xpath +
                self._account.in_service_numbers.totals._xpath
        )
        with requests_mock.Mocker() as m:
            m.get(self._account.client.config.url+
                    self._account.in_service_numbers.totals.get_xpath(),
                content=XML_RESPONSE_TOTALS)
            count = self._account.in_service_numbers.totals.get().count
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(count, "4")

    def test_line_option_orders(self):
        self.assertEquals(self._account.line_option_orders.get_xpath(),
            self._account.get_xpath()+self._account.line_option_orders._xpath)
        with requests_mock.Mocker() as m:
            m.post(self._account.client.config.url+
                    self._account.line_option_orders.get_xpath(),
                    content = XML_RESPONSE_LINE_OPTION_ORDER)
            self._account.line_option_orders.tn_line_options.add(
                {"telephone_number":"5209072453","calling_name_display":"off"}
            )
            response = self._account.line_option_orders.save()
            self.assertEquals(m.request_history[0].method, "POST")
            self.assertEquals(response.line_options.items[0].errors.error.\
                items[0].telephone_number, "5209072452")

    def test_lnpchecker(self):
        self.assertEquals(self._account.lnpchecker.get_xpath(True),
            self._account.get_xpath()+self._account.lnpchecker._xpath)
        with requests_mock.Mocker() as m:
            m.post(self._account.client.config.url+
                    self._account.lnpchecker.get_xpath(True),
                    content = XML_RESPONSE_LNP_CHECKER)
            response = self._account.lnpchecker(["123456"])
            self.assertEquals(m.request_history[0].method, "POST")
            self.assertEquals(
                response.unsupported_rate_centers.rate_center_group.items[0].\
                    city,
                "BALTIMORE")

    def test_npa_nxx(self):
        self.assertEquals(self._account.available_npa_nxx.get_xpath(),
            self._account.get_xpath() +self._account.available_npa_nxx._xpath)
        with requests_mock.Mocker() as m:
            m.get(self._account.client.config.url+
                    self._account.available_npa_nxx.get_xpath(),
                content=XML_RESPONSE_AVAILABLE_NPA_NXX_GET)
            npa = self._account.available_npa_nxx.list({"state": "CA"})
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(len(npa.items), 2)
            self.assertEquals(npa.items[0].city, "COMPTON:COMPTON DA")
            self.assertEquals(npa.items[0].npa, "424")
            self.assertEquals(npa.items[0].nxx, "242")
            self.assertEquals(npa.items[1].quantity, "5")
            self.assertEquals(npa.items[1].state, "CA")

    def test_tn_reservation_delete(self):
        res = self._account.tnreservation
        res.id = "123"
        url = self._account.client.config.url +\
            self._account.tnreservation.get_xpath()
        with requests_mock.Mocker() as m:
            m.delete(url, status_code = 200)
            res.delete()
            self.assertEquals(m.request_history[0].method, "DELETE")

    def test_tn_reservation_get(self):
        res = self._account.tnreservation
        res.id = "123"
        self.assertEquals(self._account.tnreservation.get_xpath(),
            self._account.get_xpath()+
            self._account.tnreservation._xpath.format("123"))
        url = self._account.client.config.url +\
            self._account.tnreservation.get_xpath()
        with requests_mock.Mocker() as m:
            m.get(url, content = XML_RESPONSE_TN_RESERVATION_GET)
            res.get("123")
            self.assertEquals(m.request_history[0].method, "GET")
            self.assertEquals(res.id, "0099ff73-da96-4303")

    def test_tn_reservation_save(self):
        self.assertEquals(self._account.tnreservation.get_xpath(True),
            self._account.get_xpath()+self._account.tnreservation.\
                _xpath_save)
        url = self._account.client.config.url +\
            self._account.tnreservation.get_xpath(True)
        with requests_mock.Mocker() as m:
            m.post(url, headers={"location": url + "/1337"})
            res = self._account.tnreservation
            res.reserved_tn = "123456789"
            res.save()
            self.assertEquals(m.request_history[0].method, "POST")
            self.assertEquals(res.id, "1337")

if __name__ == "__main__":
    main()