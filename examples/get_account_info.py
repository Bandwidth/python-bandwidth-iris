from iris_sdk.models.account import Account
from iris_sdk.client import Client

class GetAccountInfo():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(self._client)

        acc.get()

        print("\n--- Account info ---\n")

        print("id: " + (acc.account_id or ""))
        print("company: " + (acc.company_name or ""))
        print("customer: " + (acc.customer_name or ""))
        print("type: " + (acc.account_type or ""))
        print("description:" + (acc.description or ""))
        print("address: (" + (acc.address.address_type or "") + ")")
        print("    house no.: " + (acc.address.house_number or ""))
        print("    house prefix: " + (acc.address.house_prefix or ""))
        print("    house suffix: " + (acc.address.house_suffix or ""))
        print("    pre-directional: " + (acc.address.pre_directional or ""))
        print("    street name: " + (acc.address.street_name or ""))
        print("    street suffix: " + (acc.address.street_suffix or ""))
        print("    post-directional: " + (acc.address.post_directional or ""))
        print("    address line 2: " + (acc.address.address_line2 or ""))
        print("    city: " + (acc.address.city or ""))
        print("    state: " + (acc.address.state_code or ""))
        print("    zip: " + (acc.address.zip or ""))
        print("    plus four: " + (acc.address.plus_four or ""))
        print("    county: " + (acc.address.county or ""))
        print("    country: " + (acc.address.country or ""))
        print("contact:")
        print("    first name: " + (acc.contact.first_name or ""))
        print("    last name: " + (acc.contact.last_name or ""))
        print("    phone: " + (acc.contact.phone or ""))
        print("    email: " + (acc.contact.email or ""))
        print("reservation allowed: " + (acc.reservation_allowed or ""))
        print("lnp enabled: " + (acc.lnp_enabled or ""))
        print("port carrier type: " + (acc.port_carrier_type or ""))
        print("nena id: " + (acc.nena_id or ""))
        print("spid: " + (acc.spid or ""))
        print("alt. spid: " + (acc.alt_spid or ""))
        print("new sms account: " + (acc.is_new_sms_account or ""))

        print("tiers:")
        for tier in acc.tiers.items:
            print("    " + (tier.tier or ""))