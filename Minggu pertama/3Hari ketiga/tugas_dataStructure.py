
# Data Structure
'''
Soal 1: Perbedaan Data Structure

Jawab Pertanyaan di bawah ini:

Jelaskan perbedaan dari List, Tuple, Set dan Dictionary!

jawab :
List (Daftar):

-List adalah koleksi elemen yang dipesan dan dapat diubah (mutable) dalam Python.
-Elemen-elemen dalam list dapat memiliki tipe data yang berbeda.
-List ditandai dengan kurung siku [ ] dan elemen-elemennya dipisahkan oleh koma.

Tuple:
-Tuple adalah koleksi elemen yang dipesan dan tidak dapat diubah (immutable) dalam Python.
-Elemen-elemen dalam tuple juga dapat memiliki tipe data yang berbeda.
-Tuple ditandai dengan tanda kurung biasa ( ) atau tanpa tanda kurung.

Set:
-Set adalah kumpulan elemen yang tidak berurutan dan tidak ada elemen yang berulang dalam Python.
-Elemen-elemen dalam set juga dapat memiliki tipe data yang berbeda.
-Set ditandai dengan kurung kurawal { } atau menggunakan fungsi set().

Dictionary:
-Dictionary adalah kumpulan pasangan kunci-nilai (key-value pair) yang tidak berurutan dalam Python.
-Setiap kunci dalam dictionary harus unik.
-Dictionary ditandai dengan kurung kurawal { } dan pasangan kunci-nilai dipisahkan oleh tanda titik dua (:).

'''

#------------------------------------------------------------------
# List
'''
Soal 2: Akses List
Lengkapi kode untuk menghasilkan suatu output yang di harapkan

a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
# lengkapi disini dengan slicing list

Expected Output :

[ '13b', 'aa1', 1.32, 22.1 ]

'''
a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
slicing_list = a[1:5]
print(slicing_list)
#-------------------------------------------------------------------
'''
Soal 3: Akses Nested List
Lengkapi kode untuk menghasilkan suatu output yang di harapkan


a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
# lengkapi disini dengan subsetting list

Expected Output :


[0, 6]
'''
a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
subset_list = a[1][1:]
print(subset_list)
#---------------------------------------------------------------------
'''
Soal 4: List Manipulation

Lengkapi kode untuk menghasilkan suatu output yang di harapkan

a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
# lengkapi disini change list value



print(a)

Expected Output :

[ [5, 9, 10], [11, 0, 6] ]
'''
a = [
    [5, 9, 8],
    [0, 0, 6]
    ]

a[0][2] = 10
a[1][0] = 11

print(a)
#---------------------------------------------------------------------
'''
Soal 5: Delete Element List

Lengkapi kode untuk menghasilkan suatu output yang di harapkan


areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Hilangkan elemen yang bernilai "bathroom" dan 10.50 dalam satu statement code



print(areas)

Expected Output:

['hallway',
 11.25,
 'kitchen',
 18.0,
 'chill zone',
 20.0,
 'bedroom',
 10.75,
 'poolhouse',
 24.5,
 'garage',
 15.45]


'''
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

areas = [x for x in areas if x != "bathroom" and x != 10.50]
print(areas)
#-----------------------------------------------------------------------------------
'''
## Soal 6: List Comprehension

Gunakan metode **list comprehension** untuk mencari anggota dari S yang habis di bagi 2, kemudian assign hasilnya dalam bentuk list ke dalam variabel T.


S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = 

print(T)

Expected Output:

[0, 4, 16, 36, 64]



'''
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = [x for x in S if x % 2 == 0]

print(T)
#----------------------------------------------------------------------------------
'''
# Tuple

## Soal 7. Mengakses Tuple

Gunakan cara sclicing untuk mengakses tuple sehingga mendapatkan hasil sesuai expected output


tuple_1 = (1, 2, 6, 7, 8, 9, 10)

#akses tuple

Expected Outpout:


(6, 7, 8)



'''
tuple_1 = (1, 2, 6, 7, 8, 9, 10)

result = tuple_1[2:5]

print(result)
#-------------------------------------------------------------------------------
'''
# Dictionary

Soal 8: Menambahkan key-value baru ke Dictionary

Lengkapi kode untuk menghasilkan suatu output yang di harapkan


europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# tambahkan key itali ke objek dictionary dengan value roma


# cek apakah itali ada di dalam objek dictionary

Expected Output:
    
True

'''
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

europe['itali'] = 'roma'
key_exists = 'itali' in europe

print(key_exists)
#--------------------------------------------------------------------------------
'''
Soal 9: Update dan Remove Dictinary
    
Lengkapi kode untuk menghasilkan suatu output yang di harapkan


europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# update nilai ibukota german ke berlin


# remove australia dari europa


print(europe)

Expected Output:

{'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw'}
'''
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna'}

europe['germany'] = 'berlin'
del europe['australia']

print(europe)

#-----------------------------------------------------------------------------------
'''
Soal 10: Nested Dictionary
    
Lengkapi kode untuk menghasilkan suatu output yang di harapkan


country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } 
         }

# berapa populasi dari kota german?


# update data baru, yaitu negara indonesia dengan capital jakarta dan poulasi 250


print(country)

Expected Output:

80.62

{'spain': {'capital': 'madrid', 'population': 46.77}, 'france': {'capital': 'paris', 'population': 66.03}, 'germany': {'capital': 'berlin', 'population': 80.62}, 'norway': {'capital': 'oslo', 'population': 5.084}, 'indonesia': {'capital': 'jakarta', 'population': 250}}

'''
country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } 
         }

populasi_german = country['germany']['population']
country['indonesia'] = {'capital': 'jakarta', 'population': 250}

print(populasi_german)
print(country)
#------------------------------------------------------------------------------------
'''
Soal 11: Loop Dictionary
    
Lengkapi kode untuk menghasilkan suatu output yang di harapkan


country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 },
           'indonesia' : {'capital':'jakarta', 'population':250}
         }

for ..., .... in country.items():
    print('Ibukota '+....+' adalah ' + ....)

Expected Output:
    
Ibukota spain adalah madrid

Ibukota france adalah paris

Ibukota germany adalah berlin

Ibukota norway adalah oslo

Ibukota indonesia adalah jakarta


'''
country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 },
           'indonesia': {'capital':'jakarta', 'population':250}
         }

for country_name, country_info in country.items():
    print('Ibukota ' + country_name + ' adalah ' + country_info['capital'])

#------------------------------------------------------------------------------
'''
# Set

## Soal 12: Remove Duplicate using set


Hilangkan nilai duplikat dari sebuah objek list dengan menggunakan cara set sehingga menjadi sebuah tipe set


obj_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]

#using set

Expected output: 

{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

'''
obj_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]

unique_set = set(obj_list)

print(unique_set)
#---------------------------------------------------------------------------------
'''
## Soal 13: Mengubah dan menghapus anggota set

Ubahlah dan hapus anggota set sehingga mendapatkan hasil yang diinginkan


set_1 = {1, 2, 3, 4, 5}

#tambahkan anggota set dengan nilai {6,7,8}

#hapus nilai anggota set 8

Expected output:

{1, 2, 3, 4, 5, 6, 7}

'''
set_1 = {1, 2, 3, 4, 5}

set_1.update({6, 7, 8})
set_1.remove(8)

print(set_1)
#----------------------------------------------------------------------------------
'''
## Soal 14: Operasi pada Set

Carilah irisan dari ke dua set dengan menggunakan metode intersection


set_2 = {6, 8, 9, 10, 24}
set_3 = {6, 10, 8, 25, 13}

#intersection set

Expected output:


{6, 8, 10}


'''
set_2 = {6, 8, 9, 10, 24}
set_3 = {6, 10, 8, 25, 13}

intersection_set = sorted(set_2.intersection(set_3))

print(intersection_set)
