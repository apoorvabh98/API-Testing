'''
steps
1.Read updated json from file
2.Parse into json format
3.hit put method
4.parse respone to json format
5.validate Respone
'''
import requests
import json
from jsonpath import jsonpath

url="https://reqres.in/api/users/2"

#read input json file
#json.loads converts JSON string to Python dictionary
file=open(r"D:\python notes\createuser.json",'r')
json_input=file.read()
request_json=json.loads(json_input)

#make request with json input body
response=requests.put(url,request_json)

#Validating response code
assert response.status_code==200

#parse response content
response_json=json.loads(response.text)
print(response_json)
updated_li=jsonpath(response_json,'updatedAt')
print(updated_li)









