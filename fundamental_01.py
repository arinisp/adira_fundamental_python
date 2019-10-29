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

customer2_name = 'Sari'
customer2_jenis_kelamin = WANITA
customer2_total_income = 5500000
customer2_existing = False
customer2_occupation = FIX

customer3_name = 'Eka'
customer3_jenis_kelamin = WANITA
customer3_total_income = 4200000
customer3_existing = True
customer3_occupation = NON_FIX

if customer1_existing :
    print(f'{customer1_name} masih aktif')

if customer1_existing :
    print(f'{customer2_name} masih aktif')

if customer1_existing:
    print(f'{customer3_name} masih aktif')


print(f'{nama_program} versi{versi} oleh{author}')