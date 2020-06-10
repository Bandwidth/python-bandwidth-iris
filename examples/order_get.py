import sys
import time
from iris_sdk import Account, Client
from iris_sdk.models.data.ord.existing_search_order import ExistingSearchOrder


def search_and_order(account, site_id):
    numbers = account.available_numbers.list(
            {"areaCode": "919", "quantity": 100})
    telephone_number_to_order = numbers.items[-1]
    order = account.orders.create({
        "name": "test",
        "site_id": site_id,
        "customer_order_id": "123456789",
        "existing_telephone_number_order_type": {
            "telephone_number_list": {
                "telephone_number": [telephone_number_to_order]
            }
        }
    })
    order_id = order.id
    time.sleep(3)  # wait for order to complete
    return order_id


def list_numbers_on_order(account, order_id):
    response = account.orders.get(order_id)
    order = response.order
    original_payload: ExistingSearchOrder = order.existing_telephone_number_order_type
    original_numbers = original_payload.telephone_number_list
    failed_quantity = response.failed_quantity
    failed_numbers = response.failed_numbers
    completed_quantity = response.completed_quantity
    completed_numbers = response.completed_numbers
    print("Tried to order Numbers:")
    for number in original_numbers.items:
        print(number)
    print(f"Of those numbers, {completed_quantity} were successful:")
    for number in response.completed_numbers.items:
        print(number)
    print(f"Of those numbers, {failed_quantity} were unsuccessful:")
    for number in response.failed_numbers.items:
        print(number)
    return


if __name__ == '__main__':
    my_account = Account(client=Client(filename="config.cfg")) # Comment this line to use the config file
    # Uncomment these lines to use environment variables
    # BANDWIDTH_ACCOUNT_ID = os.environ["BANDWIDTH_ACCOUNT_ID"]
    # BANDWIDTH_API_USER = os.environ["BANDWIDTH_API_USER"]
    # BANDWIDTH_API_PASSWORD = os.environ["BANDWIDTH_API_PASSWORD"]
    # client = Client(url="https://dashboard.bandwidth.com/api",
    #                 account_id=BANDWIDTH_ACCOUNT_ID,
    #                 username=BANDWIDTH_API_USER,
    #                 password=BANDWIDTH_API_PASSWORD)
    # my_account = Account(client=client)

    if len(sys.argv) < 2:
        sys.exit("usage: python order_get.py [site/subbacount-id], e.g.:" +
                 "\npython order_get.py 23360")
    my_site_id = sys.argv[1]
    my_order_id = search_and_order(my_account, my_site_id)
    list_numbers_on_order(my_account, my_order_id)
