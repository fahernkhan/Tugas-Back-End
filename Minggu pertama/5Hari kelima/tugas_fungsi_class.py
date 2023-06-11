'''
Soal 1: Membuat Simple Function
Buatlah suatu fungsi yang menerima satu input argumen berbentuk list dan mempunyai elemen bertipe numeric semua, 
dimana fungsi tersebut berguna untuk menghitung rata2 dari kumpulan elemen list tersebut. beri nama fungsi tersebut "mean_list"

Expected Output:
12.39
'''

'''obj_list = [11.25, 18.0, 20.0, 10.75, 9.50, 13.45, 23.0, 7.0, 8.45, 2.50]
def mean_list(inp_list):
    pass
    #lengkapi kode ini
 

print(mean_list(obj_list))
'''
obj_list = [11.25, 18.0, 20.0, 10.75, 9.50, 13.45, 23.0, 7.0, 8.45, 2.50]

def mean_list(inp_list):
    total = sum(inp_list)
    mean = total / len(inp_list)
    return mean

print(mean_list(obj_list))


'''
Soal 2. Mapping Fungsi lambda
Hitunglah jumlah bilangan genap dari sebuah objek list berikut menggunakan lambda function

Expected output:
500
'''

'''obj_list = [i for i in range(1000)]

#lengkapi kode ini dengan fungsi lambda yang diaplikasikan pada obj_list


print(hasil)
'''
obj_list = [i for i in range(1000)]

hasil = sum(filter(lambda x: x % 2 == 0, obj_list))

print(hasil)