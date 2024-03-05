
# # import urllib library 
# from urllib.request import urlopen 
# import json 
# url = "https://dummyjson.com/products"
# response = urlopen(url) 
# data_json = json.loads(response.read())
# distinct_pro = []
# for rec in data_json["products"]:
#     if rec['category'] not in distinct_pro:
#         distinct_pro.append(rec['category'])
# print(data_json)


import requests
import ast
url = "https://api.rajaongkir.com/starter/province"

payload = {}
headers = {
  'key': '8dc9e7af902189fe4210b56af68ca959'
}

response = requests.request("GET", url, headers=headers, data=payload)
# import ipdb; ipdb.set_trace()
data_tup = response.json().items()
for rec in data_tup:
    print(type(rec), rec)
# print(response.text, type(data_json), data_json)