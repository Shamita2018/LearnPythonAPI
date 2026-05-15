import requests
import json
import random
import string
import time
#base url
base_url = "https://gorest.co.in"

#auth token
auth_token= "Bearer cdebdd9c0b9a192e46660843d6353deb8f2470cc80894a02e33ae612f6d39bdb"

def generate_random_email():
    domain = "example.com"
    email_len= 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_len))
    email = random_string + "@" + domain
    print(email)
    return email 


#get request
def my_function_get():
    #print("json response body")
    url = base_url + "/public/v2/users/"
    headers = {"Authorization":auth_token}
    response = requests.get(url,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str= json.dumps(json_data,indent=4)
    print(" GET json response body", json_str)
  


def my_function_post():
    url = base_url + "/public/v2/users/"
    payload = {
    "name": "Shamita",
    "email": f"shamita-{int(time.time())}@example.com",
    "gender": "female",
    "status": "active",
}
    headers = {"Authorization":auth_token}
    response = requests.post(url,data=payload, headers=headers)
    assert response.status_code == 201
    json_data=response.json()
    json_str= json.dumps(json_data,indent=4)
    print("POST json response body", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Shamita"
    return user_id

def my_function_put(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    payload = {
    "name": "ShamitaMalik",
    "email": f"shamitaMalik-{int(time.time())}@example.com",
    "gender": "female",
    "status": "inactive"
}
    headers = {"Authorization":auth_token}
    response = requests.put(url,data=payload, headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str= json.dumps(json_data,indent=4)
    print("PUT json response body", json_str)
    assert json_data["id"] == user_id


def my_function_delete(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    headers = {"Authorization":auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("Delete user is done")
   

#userid = my_function_post()
#my_function_put(userid)
#my_function_delete(userid)
generate_random_email()