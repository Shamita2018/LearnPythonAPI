import random
import requests
import json



# payload = {
#     "id": 0,
#     "petId": 0,
#     "quantity": 0,
#     "shipDate": "2026-05-07T12:40:52.674Z",
#     "status": "placed",
#     "complete": True
# }
mypayload=open("data.json","r").read()
response = requests.post(
    "https://petstore.swagger.io/v2/store/order",
    json=json.loads(mypayload)
)

print(response.status_code)
print(response.json())
assert response.json()['status']=='placed', "status not matched"
assert response.json()['id']!=None, "coming as empty"