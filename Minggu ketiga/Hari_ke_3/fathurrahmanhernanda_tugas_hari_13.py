import requests
import json


#Ambil data faskes vaksin untuk kota bandung
params = {
    
    "city":"KOTA BANDUNG"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

url = "https://kipi.covid19.go.id/api/get-faskes-vaksinasi"
response = requests.get(url, params=params, headers=headers)

print(response.status_code)
print(response.text)
text = json.dumps(response.json(), sort_keys=True, indent=4)
print(text)
print("\n")

# Ambil data JSON dari respons
data = response.json()
# Ambil data faskes vaksinasi saja dari respons
faskes_data = data.get("data", [])

# Sort data berdasarkan total sukses vaksin 1
faskes_sorted_by_vaksin1 = sorted(faskes_data, key=lambda x: x.get("vaksinasi1_sukses", 0), reverse=True)

# Tampilkan 5 faskes dengan total sukses vaksin 1 terbanyak
print("Faskes dengan total sukses vaksin 1 terbanyak:")
for faskes in faskes_sorted_by_vaksin1[:5]:
    print("Nama Faskes:", faskes.get("nama"))
    print("---")

print("\n")

# Sort data berdasarkan total sukses vaksin 2
faskes_sorted_by_vaksin2 = sorted(faskes_data, key=lambda x: x.get("vaksinasi2_sukses", 0), reverse=True)

# Tampilkan 5 faskes dengan total sukses vaksin 2 terbanyak
print("Faskes dengan total sukses vaksin 2 terbanyak:")
for faskes in faskes_sorted_by_vaksin2[:5]:
    print("Nama Faskes:", faskes.get("nama"))
    print("---")

