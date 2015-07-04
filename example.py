from examples.get_account_info import GetAccountInfo
from examples.get_available_numbers import GetAvailableNumbers
from examples.get_in_service_numbers import GetInServiceNumbers
from examples.pagination import Pagination
from examples.get_sites import GetSites

FILENAME = "examples/config.cfg"

GetAccountInfo(FILENAME)
GetAvailableNumbers(FILENAME)
GetInServiceNumbers(FILENAME)
Pagination(FILENAME)
GetSites(FILENAME)