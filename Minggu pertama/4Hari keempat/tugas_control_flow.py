'''Soal 1: If-Else Statement

Lengkapi kode untuk menghasilkan suatu output yang di harapkan

- Bualah sebuah if-else statement yang dimana akan mem-print 'High' jika grade adalah 'A' dan price lebih dari 100000, kemudian mem-print 'Medium' jika grade adalah 'A' dan price lebih dari 50000 dan memprint 'low' jika grade adalah 'A' dan price lebih kecil dan sama dengan 50000.
'''
grade = 'A'  # Ganti dengan nilai grade yang sesuai
price = 60000  # Ganti dengan nilai price yang sesuai

if grade == 'A':
    if price > 100000:
        print('High')
    elif price > 50000:
        print('Medium')
    else:
        print('Low')
print("")
#kerjakan di bawah ini

'''Soal 2: For Loop

Lengkapi kode untuk menghasilkan suatu output yang diharapkan:
*   Cari siswa mana saja yang memiliki nilai lebih dari sama dengan 80. Masukkan kedalam sebuah list. print hasilnya

Expected output:

['Budi', 'Rudi', 'Leo']

'''

#kerjakan di bawah ini

'''data_siswa = [
    {
        "nama":"Budi",
        "nilai": 90
    },
    {
        "nama":"Nina",
        "nilai": 78
    },
    {
        "nama":"Rudi",
        "nilai": 91
    },
    {
        "nama":"Olivia",
        "nilai": 76
    },
    {
        "nama":"Leo",
        "nilai": 80
    },
    {
        "nama":"Liam",
        "nilai": 67
    },
    {
        "nama":"Sheila",
        "nilai": 76
    }
]
'''
#kerjakan di bawah ini

'''Soal 2: For Loop

Lengkapi kode untuk menghasilkan suatu output yang diharapkan:
*   Cari siswa mana saja yang memiliki nilai lebih dari sama dengan 80. Masukkan kedalam sebuah list. print hasilnya

Expected output:

['Budi', 'Rudi', 'Leo']

'''

#kerjakan di bawah ini

data_siswa = [
    {
        "nama": "Budi",
        "nilai": 90
    },
    {
        "nama": "Nina",
        "nilai": 78
    },
    {
        "nama": "Rudi",
        "nilai": 91
    },
    {
        "nama": "Olivia",
        "nilai": 76
    },
    {
        "nama": "Leo",
        "nilai": 80
    },
    {
        "nama": "Liam",
        "nilai": 67
    },
    {
        "nama": "Sheila",
        "nilai": 76
    }
]

siswa_lebih_80 = []
for siswa in data_siswa:
    if siswa['nilai'] >= 80:
        siswa_lebih_80.append(siswa['nama'])

print(siswa_lebih_80)

