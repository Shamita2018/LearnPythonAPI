import requests
resp = requests.get("https://petstore.swagger.io/v2/store/inventory")
json_response= resp.json()
print(json_response['sold'])
print(json_response['pending'])
#print(resp)
#print(type(resp))
#print(dir(resp))
#print(resp.text)
#print("----------------")
#print(resp.content)
#print("********")
print(resp.json())
print(resp.headers)
print(resp.url)
#print("********")
code=resp.status_code
assert code==200, "Code doesn't match"
assert json_response["pending"]!=None, "failed"

