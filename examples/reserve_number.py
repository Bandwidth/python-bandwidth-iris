from iris_sdk.models.account import Account
from iris_sdk.client import Client

class ReserveNumber():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- Reserving number ---\n")

        available_numbers = \
            acc.available_numbers.list({"areaCode": "435"})

        phone_number = available_numbers.items[0]
        if (phone_number is None):
            print("No available numbers")
            return

        reservation = acc.tnreservation
        reservation.reserved_tn = phone_number.telephone_number
        reservation.save()
        print(phone_number.telephone_number + " reserved:")
        reservation.get()
        print("    reservation id: " + (reservation.reservation_id or ""))
        print("    expires: " + (reservation.reservation_expires or ""))