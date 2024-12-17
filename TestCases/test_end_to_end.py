import requests
import json
import jsonpath

def test_Add_New_Data():
    App_url="https://thetestingworldapi.com/api/studentsDetails"
    f=open(r"D:\python notes\Request_json.json",'r')
    request_json=json.loads(f.read())
    response=requests.post(App_url,request_json)
    print(response.text)
    id=jsonpath.jsonpath(response.json(),"id")
    print(id)

    tech_api_url="https://thetestingworldapi.com/api/technicalskills"
    f=open(r"D:\python notes\TechDetails.json",'r')
    request_json=json.loads(f.read())
    request_json['id']=int(id[0])
    request_json['st_id']=id[0]
    response=requests.post(tech_api_url,request_json)
    print(response.text)

    add_api_url="https://thetestingworldapi.com/api/addresses"
    f=open(r"D:\python notes\Address.json","r")
    request_json=json.loads(f.read())
    request_json['stId']=id[0]
    response=requests.post(add_api_url,request_json)

    final_details="https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response=requests.get(final_details)
    print(response.text)








