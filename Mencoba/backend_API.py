import requests
import json

response = requests.get("http://dev.farizdotid.com/api/daerahindonesia/provinsi")

print(response.status_code)
print(response.text)
print("\n\n")
#melihat semua kota yang ada di provinsi tertentu
params = {
    "id_provinsi":32
}

response = requests.get("https://dev.farizdotid.com/api/daerahindonesia/kota",params=params)

print(response.status_code)
print(response.text)
text = json.dumps(response.json(), sort_keys=True, indent=4)
print(text)