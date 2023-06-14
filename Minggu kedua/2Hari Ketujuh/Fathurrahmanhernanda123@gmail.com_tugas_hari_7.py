#Nomor 1
def read_txt(fname):
    try:
        with open(fname, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File tidak ditemukan.")

# Memanggil fungsi read_txt dengan memberikan path lengkap ke file sebagai input
read_txt(r"H:\Tugas Back End\Minggu kedua\2Hari Ketujuh\berkas_fileHandling\1.txt")


#Nomor 2
import json

def read_covid():
    file = r'H:\Tugas Back End\Minggu kedua\2Hari Ketujuh\berkas_fileHandling\2.json'
    
    with open(file, 'r') as file:
        data = json.load(file)
        cases = [entry['Cases'] for entry in data]
        return cases

# Memanggil fungsi read_covid
cases = read_covid()
print(cases)