import requests
import json
import sys,json



BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id):
    import pdb
    pdb.set_trace()
    resp = requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.status_code)
    print(resp.json())

id = input("Enter some ID: ")
get_resource(id)