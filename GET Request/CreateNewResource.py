import requests
import json

from jsonpath import jsonpath

url="https://reqres.in/api/users"

#read input json file
file=open(r"D:\python notes\createuser.json","r")
json_input=file.read()
request_json=json.loads(json_input)
#print(request_json)

#make a POST request with json input body

response=requests.post(url,request_json)
# print(response)
print(response.content)
# assert response.status_code==201
#print(response.headers)
print(response.headers.get("Content-Length"))

#parse response to json
response_json=json.loads(response.text)
print(response_json)

#picking up id
id=jsonpath(response_json,'id')
print(id)