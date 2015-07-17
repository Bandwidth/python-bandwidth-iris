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
    b"    <PartnerSupportedRateCenters>"
    b"        <RateCenterGroup>"
    b"            <RateCenter>FT COLLINS</RateCenter>"
    b"            <City>FORT COLLINS</City>"
    b"            <State>CO</State>"
    b"            <LATA>656</LATA>"
    b"            <Tiers>"
    b"                <Tier>1</Tier>"
    b"            </Tiers>"
    b"            <TnList>"
    b"                <Tn>4109235436</Tn>"
    b"            </TnList>"
    b"        </RateCenterGroup>"
    b"    </PartnerSupportedRateCenters>"
    b"    <SupportedLosingCarriers>"
    b"        <LosingCarrierTnList>"
    b"            <LosingCarrierSPID>9998</LosingCarrierSPID>"
    b"            <LosingCarrierName>Carrier L3</LosingCarrierName>"
    b"            <LosingCarrierIsWireless>false</LosingCarrierIsWireless>"
    b"            <LosingCarrierAccountNumberRequired>false</LosingCarrierAccountNumberRequired>"
    b"            <LosingCarrierMinimumPortingInterval>5</LosingCarrierMinimumPortingInterval>"
    b"            <TnList>"
    b"                <Tn>4109255199</Tn>"
    b"                <Tn>4104685864</Tn>"
    b"                <Tn>4103431313</Tn>"
    b"                <Tn>4103431561</Tn>"
    b"            </TnList>"
    b"        </LosingCarrierTnList>"
    b"    </SupportedLosingCarriers>"
    b"    <UnsupportedLosingCarriers />"
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

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url + self._account.get_xpath()
            m.get(url, content=XML_RESPONSE_ACCOUNT_GET)

            self._account.get()

            self.assertEqual(self._account.id, "123456")
            self.assertEqual(self._account.company_name, "Spam")
            self.assertEqual(self._account.account_type, "Ham")
            self.assertEqual(self._account.tiers.tier.items, ["0"])
            self.assertEqual(self._account.address.house_number, "900")
            self.assertEqual(self._account.contact.first_name, "Eggs")

    def test_available_numbers(self):

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                    self._account.available_numbers.get_xpath()
            m.get(url, content=XML_RESPONSE_AVAILABLE_NUMBERS_GET)

            avail_numbers = self._account.available_numbers.list(
                {"state": "NJ"})

            self.assertEqual(avail_numbers.items,
                ["6093252507", "6093570994", "6093574598"])
            self.assertEqual(self._account.available_numbers.result_count,
                "3")

    def test_available_numbers_detail(self):

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                self._account.available_numbers.get_xpath()
            m.get(url, content=XML_RESPONSE_AVAILABLE_NUMBERS_DETAIL_GET)

            avail_numbers = self._account.available_numbers.list(
                {"enableTNDetail": "true", "state": "NJ"})

            self.assertEqual(avail_numbers.items[0].city, "ALLENTOWN")
            self.assertEqual(avail_numbers.items[0].lata, "222")
            self.assertEqual(avail_numbers.items[1].full_number,"6093570994")
            self.assertEqual(avail_numbers.items[1].tier, "0")
            self.assertEqual(avail_numbers.items[2].vendor_id, "49")
            self.assertEqual(avail_numbers.items[2].vendor_name,
                "Bandwidth CLEC")
            self.assertEqual(self._account.available_numbers.result_count,"3")

    def test_available_numbers_error(self):

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                self._account.available_numbers.get_xpath()
            m.get(url, content=XML_RESPONSE_AVAILABLE_NUMBERS_ERROR,
                status_code=400)

            with self.assertRaises(RestError):
                self._account.available_numbers.list(None)

    def test_disc_numbers(self):

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                self._account.disconnected_numbers.get_xpath()
            m.get(url, content=XML_RESPONSE_DISCONNECTED_NUMBERS_GET)

            disc_numbers = self._account.disconnected_numbers.list(
                {"page": 1, "type": "x"})

            self.assertEqual(disc_numbers.items, ["4158714245","4352154439"])

    def test_disc_numbers_totals(self):

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                self._account.disconnected_numbers.totals.get_xpath()
            m.get(url, content=XML_RESPONSE_TOTALS)

            count = self._account.disconnected_numbers.totals.get().count
            self.assertEqual(count, "4")

    def test_in_service_numbers(self):

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                self._account.in_service_numbers.get_xpath()
            m.get(url, content=XML_RESPONSE_DISCONNECTED_NUMBERS_GET)

            numbers = self._account.in_service_numbers.list({"state": "NJ"})

            self.assertEqual(numbers.items,["4158714245","4352154439"])
            self.assertEqual(self._account.in_service_numbers.total_count,"4")

    def test_in_service_numbers_totals(self):

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                self._account.in_service_numbers.totals.get_xpath()
            m.get(url, content=XML_RESPONSE_TOTALS)

            count = self._account.in_service_numbers.totals.get().count
            self.assertEqual(count, "4")

    def test_line_option_orders(self):

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                self._account.line_option_orders.get_xpath()
            m.post(url, content = XML_RESPONSE_LINE_OPTION_ORDER)

            self._account.line_option_orders.tn_line_options.add(
                {"telephone_number":"5209072453","calling_name_display":"off"}
            )

            response = self._account.line_option_orders.save()

            self.assertEqual(response.line_options.items[0].errors.error.\
                items[0].telephone_number, "5209072452")

    def test_lnpchecker(self):

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                self._account.lnpchecker.get_xpath(True)
            m.post(url, content = XML_RESPONSE_LNP_CHECKER)

            response = self._account.lnpchecker(["123456"])

            grp = response.unsupported_rate_centers.rate_center_group.items[0]

            self.assertEqual(grp.rate_center, "BALTIMORE")
            self.assertEqual(grp.city, "BALTIMORE")
            self.assertEqual(grp.state, "MD")
            self.assertEqual(grp.lata, "238")
            self.assertEqual(grp.tn_list.tn.items,["4109255199","4104685864"])

            grp = response.unsupported_rate_centers.rate_center_group.items[1]

            self.assertEqual(grp.rate_center, "SPARKSGLNC")
            self.assertEqual(grp.city, "SPARKS GLENCOE")
            self.assertEqual(grp.state, "MD")
            self.assertEqual(grp.lata, "238")
            self.assertEqual(grp.tn_list.tn.items,["4103431313","4103431561"])

            grp = response.partner_supported_rate_centers.rate_center_group.\
                items[0]

            self.assertEqual(grp.rate_center, "FT COLLINS")
            self.assertEqual(grp.city, "FORT COLLINS")
            self.assertEqual(grp.state, "CO")
            self.assertEqual(grp.lata, "656")
            self.assertEqual(grp.tn_list.tn.items, ["4109235436"])
            self.assertEqual(grp.tiers.tier.items, ["1"])

            grp = response.supported_losing_carriers.losing_carrier_tn_list

            self.assertEqual(grp.losing_carrier_spid, "9998")
            self.assertEqual(grp.losing_carrier_name, "Carrier L3")
            self.assertEqual(grp.losing_carrier_is_wireless, "false")
            self.assertEqual(grp.losing_carrier_account_number_required,
                "false")
            self.assertEqual(grp.losing_carrier_minimum_porting_interval,"5")
            self.assertEqual(grp.tn_list.tn.items,
                ["4109255199","4104685864","4103431313","4103431561"])

    def test_npa_nxx(self):

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                    self._account.available_npa_nxx.get_xpath()
            m.get(url, content=XML_RESPONSE_AVAILABLE_NPA_NXX_GET)

            npa = self._account.available_npa_nxx.list({"state": "CA"})

            self.assertEqual(len(npa.items), 2)
            self.assertEqual(npa.items[0].city, "COMPTON:COMPTON DA")
            self.assertEqual(npa.items[0].npa, "424")
            self.assertEqual(npa.items[0].nxx, "242")
            self.assertEqual(npa.items[1].quantity, "5")
            self.assertEqual(npa.items[1].state, "CA")

    def test_tn_reservation_delete(self):
        res = self._account.tnreservation
        res.id = "123"
        url = self._account.client.config.url +\
            self._account.tnreservation.get_xpath()

        with requests_mock.Mocker() as m:
            m.delete(url, status_code = 200)
            res.delete()

    def test_tn_reservation_get(self):

        res = self._account.tnreservation
        res.id = "123"

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                self._account.tnreservation.get_xpath()
            m.get(url, content = XML_RESPONSE_TN_RESERVATION_GET)

            res.get("123")

            self.assertEqual(res.id, "0099ff73-da96-4303")
            self.assertEqual(res.reserved_tn, "2512027430")
            self.assertEqual(res.account_id, "14")
            self.assertEqual(res.reservation_expires, "0")

    def test_tn_reservation_save(self):

        with requests_mock.Mocker() as m:

            url = self._account.client.config.url +\
                self._account.tnreservation.get_xpath(True)
            m.post(url, headers={"location": url + "/1337"})

            res = self._account.tnreservation
            res.reserved_tn = "123456789"
            res.save()

            self.assertEqual(m.request_history[0].method, "POST")
            self.assertEqual(res.id, "1337")
            self.assertEqual(res.reserved_tn, "123456789")

if __name__ == "__main__":
    main()