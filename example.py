from examples.get_account_info import GetAccountInfoExample
from examples.get_available_numbers import GetAvailableNumbersExample
from examples.get_in_service_numbers import GetInServiceNumbersExample
from examples.get_orders import GetOrdersExample

URL = "https://foo.bar"
ACCOUNT_ID = 123456789
USER_NAME = "user"
PASSWORD = "pass"

GetAccountInfoExample(URL, ACCOUNT_ID, USER_NAME, PASSWORD)
GetAvailableNumbersExample(URL, ACCOUNT_ID, USER_NAME, PASSWORD)
GetInServiceNumbersExample(URL, ACCOUNT_ID, USER_NAME, PASSWORD)
GetOrdersExample(URL, ACCOUNT_ID, USER_NAME, PASSWORD)