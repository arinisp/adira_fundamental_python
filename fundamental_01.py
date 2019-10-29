"""
Author : Bani
Purpose : Fundamental of Python
"""
print("Hello, World")

"""
Fundamental ada tiga :
1. Sequential
2. Branching
3. Loop / Pengulangan
4. Modularization :
    - Dengan fungsi
    - Dengan Class
    - Dengan Package
    
Kasus : 
Advis jenis motor bagi customer tertentu
    Step :
    1. Fundamental
    2. Data acquisition
    3. Machine Learning
"""

versi = '0.1' #tipe data string / text
nama_program = 'Customer Advisor Management System' #variable gaboleh pake spasi atau angka di depan
author = 'Arini Sri Purbani'

PRIA, WANITA = range(2) #tipe data enumerasi, konstanta sebaiknya huruf besar tp ga wajib hanya sebaiknya
FIX, NON_FIX = range(2)

customer1_name = 'Boni'
customer1_jenis_kelamin = PRIA
customer1_total_income = 3500000
customer1_existing = True
customer1_occupation = FIX
customer1_alamat = {
    'Line 1' : 'Kemanggisan',
    'Kelurahan' : 'Setiabudi',
    'Kecamatan' : 'Setiabudi',
    'City' : 'Jakarta Selatan',
    'Provinsi' : 'DKI Jakarta',
    'ZIP Code' : '16444',
    'Country' : 'Indonesia'
}

customer2_name = 'Sari'
customer2_jenis_kelamin = WANITA
customer2_total_income = 5500000
customer2_existing = False
customer2_occupation = FIX
customer2_alamat = {
    'Line 1' : 'Kemanggisan',
    'Kelurahan' : 'Setiabudi',
    'Kecamatan' : 'Setiabudi',
    'City' : 'Jakarta Selatan',
    'Provinsi' : 'DKI Jakarta',
    'ZIP Code' : '16444',
    'Country' : 'Indonesia'
}

customer3_name = 'Eka'
customer3_jenis_kelamin = WANITA
customer3_total_income = 10000000
customer3_existing = True
customer3_occupation = NON_FIX
customer3_alamat = {
    'Line 1' : 'Kemanggisan',
    'Kelurahan' : 'Setiabudi',
    'Kecamatan' : 'Setiabudi',
    'City' : 'Jakarta Selatan',
    'Provinsi' : 'DKI Jakarta',
    'ZIP Code' : '16444',
    'Country' : 'Indonesia'
}

if customer1_existing :
    print(f'{customer1_name} masih aktif')
else:
    print(f'{customer1_name} tidak aktif')

if customer2_existing :
    print(f'{customer2_name} masih aktif')
else:
    print(f'{customer2_name} tidak aktif')

if customer3_existing:
    print(f'{customer3_name} masih aktif')
else:
    print(f'{customer3name} tidak aktif')

#kasus1 customer 1 income range : <3jt, 3jt-6jt, 6jt-9jt
print (f'Pengecekan gaji {customer1_name} sebesar {customer1_total_income}')
if customer1_total_income < 3000000 :
    print('Gaji terlalu rendah')
elif customer1_total_income >= 3000000 and customer1_total_income < 6000000:
    print('Kelas menengah')
elif customer1_total_income >= 6000000 and customer1_total_income < 9000000:
    print('Kelas atas')
else:
    print('Gaji tinggi banget')

#coba cetak semua nama customer

#tanpa list
print(customer1_name, customer2_name, customer3_name)

#dengan list
print('Daftar customer')
customers = [customer1_name, customer2_name, customer3_name]
for i in range (0, len (customers)) :
    print (f'{i+1}. {customers[i]}')

print(customer1_alamat)
print(customer1_alamat['Line 1'])
print(customer1_alamat['Kelurahan'])
print(customer1_alamat['Kecamatan'])
print(customer1_alamat['City'])
print(customer1_alamat['Provinsi'])
print(customer1_alamat['ZIP Code'])
print(customer1_alamat['Country'])

#cetak customer di list/array
print(customers[0])

#simpan customer di array
#customers_by_name = dict() spt ini bisa
customers_income_by_name = {} #ini juga bisa
customers_income_by_name [customer1_name] = customer1_total_income
customers_income_by_name [customer2_name] = customer2_total_income
customers_income_by_name [customer3_name] = customer3_total_income

print ('Alamat customer by name')
for name in customers_income_by_name:
    total_income = customers_income_by_name[name]
    print(f'{name} total_income = {total_income}')