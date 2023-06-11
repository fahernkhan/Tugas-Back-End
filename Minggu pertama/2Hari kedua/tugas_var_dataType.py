"""<h2>Soal 1: Hello World to Python</h2>
    
Print Say Hello World to Python
"""
print("Hello World")

print("")
"""Expected Output : 

Hello World Python

<h2>Soal 2: Aritmatika di Python </h2>
    
- Buat statement pertambahan antara 2 number di Python
- Buat statement perkurangan antara 2 number di Python
- Buat statement perkalian antara 2 number di Python
- Buat statement pembagian antara 2 number di Python
"""
#Statement pertambahan antara 2 angka:
a = 5
b = 3
hasil = a + b
print(hasil)  # Output: 8

#Statement perkurangan antara 2 angka:
a = 5
b = 3
hasil = a - b
print(hasil)  # Output: 2

#Statement perkalian antara 2 angka:
a = 5
b = 3
hasil = a * b
print(hasil)  # Output: 15

#Statement pembagian antara 2 angka:
a = 6
b = 2
hasil = a / b
print(hasil)  # Output: 3.0

print("")
"""<h2>Quiz 3: Assign Variable dan Tipe Data Integer, Float </h2>

- Buat suatu variabel a dan b, dimana a dan b adalah nilai bertipe data numeric
- Berikan suatu nilai bertipe data integer, hasil pembagian dari a dengan b
- Berikan suatu nilai bertipe data float, hasil pembagian dari a dengan b
"""
a = 10  # nilai variabel a bertipe data integer
b = 3   # nilai variabel b bertipe data integer

hasil_integer = a // b  # hasil pembagian a dengan b, bertipe data integer
hasil_float = a / b     # hasil pembagian a dengan b, bertipe data float

print("Hasil Integer:", hasil_integer)  # Output: 3
print("Hasil Float:", hasil_float)      # Output: 3.3333333333333335

print("")
"""<h2>Soal 4: String Operation </h2>

- masukan nama depan kamu kedalam suatu variable firstname
- masukan nama belakang kamu kedalam suatu variable lastname
- tampilkan suatu kalimat 'Hello sanbercode, saya firstname lastname! saya siap belajar python backend development.'
"""



"""Expected Output :

Hello sanbercode, saya Afrida Hafizhatul Ulum! saya siap belajar python backend development.
"""
firstname = "Afrida"  # Ganti dengan nama depan Anda
lastname = "Hafizhatul Ulum"   # Ganti dengan nama belakang Anda

kalimat = "Hello sanbercode, saya " + firstname + " " + lastname + "! saya siap belajar python backend development."

print(kalimat)

print("")
"""
<h2>Soal 5: Tipe Data</h2>

Lengkapi code di bawah ini untuk menghasilkan output yang sesuai

usia =
kata = 'usiaku: '
print(kata + ...(usia)+....)
"""

"""Expected Output : (sesuai usia masing-masing)

usiaku: 28 tahun
"""
usia = 28  # Ganti dengan usia Anda

kata = 'usiaku: '
print(kata + str(usia) + ' tahun')