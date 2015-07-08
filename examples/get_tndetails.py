from iris_sdk.models.tns import Tns
from iris_sdk.client import Client

class GetTndetails():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        tns = Tns(client=self._client)

        print("\n--- TN details ---\n")

        details = tns.get(7576768750).tndetails.get()

        print(details.full_number or "")
        print("    account: " + (details.account_id or ""))
        print("    city: " + (details.city or ""))
        print("    last modified: " + (details.last_modified_date or ""))
        print("    LATA: " + (details.lata or ""))
        print("    rate center: " + (details.rate_center or ""))
        print("    state: " + (details.state or ""))
        print("    status: " + (details.status or ""))
        print("    vendor id: " + (details.vendor_id or ""))
        print("    vendor name: " + (details.vendor_name or ""))

        print("    dlda")
        print("        city: " + (details.features.dlda.address.city or ""))
        print("        listing: ")
        print("            first name" + \
            (details.features.dlda.listing_name.first_name or ""))
        print("            last name" + \
            (details.features.dlda.listing_name.last_name or ""))
        print("    lidb")
        print("        status: " + (details.features.lidb.status or ""))