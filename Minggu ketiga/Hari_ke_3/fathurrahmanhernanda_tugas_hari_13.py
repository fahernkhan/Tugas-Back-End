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



data = json.loads(response.text)
# Tampilkan 5 faskes dengan total sukses vaksin 1 terbanyak
data_faskes = data['data']
sorted_faskes_vaksin1 = sorted(data_faskes, key=lambda x: x['detail'][0]['divaksin_1'], reverse=True)[:5]
print("\n5 Faskes dengan total sukses vaksin 1 terbanyak:")
for faskes in sorted_faskes_vaksin1:
    print(f"- {faskes['nama']}: {faskes['detail'][0]['divaksin_1']} vaksin")

# Tampilkan 5 faskes dengan total sukses vaksin 2 terbanyak
sorted_faskes_vaksin2 = sorted(data_faskes, key=lambda x: x['detail'][0]['divaksin_2'], reverse=True)[:5]
print("\n5 Faskes dengan total sukses vaksin 2 terbanyak:")
for faskes in sorted_faskes_vaksin2:
    print(f"- {faskes['nama']}: {faskes['detail'][0]['divaksin_2']} vaksin")

