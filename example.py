from iris_sdk.account import Account
from iris_sdk.client import Client

client = Client(
    url="https://api.test.inetwork.com/v1.0",
    account_id=123456,
    username="",
    password=""
)

acc = Account(client)
acc.get()

print(acc.account_id)
print(acc.company_name)
print(acc.address.house_number)
print(acc.contact.first_name)
print(acc.tiers.tier[0])


lst = acc.available_numbers.list({"areaCode": "435"})
for num in lst:
    print(num)
