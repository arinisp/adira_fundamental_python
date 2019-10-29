"""
Modularization ada 3 :
1. Function
2. Class
3. Package

"""

versi = '0.15'  # tipe data string / text
nama_program = 'Customer Advisor Management System'  # variable gaboleh pake spasi atau angka di depan
author = 'Arini Sri Purbani'

PRIA, WANITA = range(2)  # tipe data enumerasi, konstanta sebaiknya huruf besar tp ga wajib hanya sebaiknya
FIX, NON_FIX = range(2)

customer1_name = 'Boni'
customer1_jenis_kelamin = PRIA
customer1_total_income = 3500000
customer1_existing = True
customer1_occupation = FIX
customer1_alamat = {
    'Line 1': 'Kemanggisan',
    'Kelurahan': 'Setiabudi',
    'Kecamatan': 'Setiabudi',
    'City': 'Jakarta Selatan',
    'Provinsi': 'DKI Jakarta',
    'ZIP Code': '16444',
    'Country': 'Indonesia'
}

customer2_name = 'Sari'
customer2_jenis_kelamin = WANITA
customer2_total_income = 5500000
customer2_existing = False
customer2_occupation = FIX
customer2_alamat = {
    'Line 1': 'Kemanggisan',
    'Kelurahan': 'Setiabudi',
    'Kecamatan': 'Setiabudi',
    'City': 'Jakarta Selatan',
    'Provinsi': 'DKI Jakarta',
    'ZIP Code': '16444',
    'Country': 'Indonesia'
}

customer3_name = 'Eka'
customer3_jenis_kelamin = WANITA
customer3_total_income = 10000000
customer3_existing = True
customer3_occupation = NON_FIX
customer3_alamat = {
    'Line 1': 'Kemanggisan',
    'Kelurahan': 'Setiabudi',
    'Kecamatan': 'Setiabudi',
    'City': 'Jakarta Selatan',
    'Provinsi': 'DKI Jakarta',
    'ZIP Code': '16444',
    'Country': 'Indonesia'
}

def check_status_peminjaman (name, is_existing) :
    if is_existing:
        print(f'{name} masih aktif')
    else:
        print(f'{name} tidak aktif')

check_status_peminjaman(customer1_name, customer1_existing)
check_status_peminjaman(customer2_name, customer2_existing)
check_status_peminjaman(customer3_name, customer3_existing)

def check_income (name, income) :
    result = ''
    if customer1_total_income < 3000000 :
        result = 'Gaji terlalu rendah'
    elif customer1_total_income >= 3000000 and customer1_total_income < 6000000:
        result = 'Kelas menengah'
    elif customer1_total_income >= 6000000 and customer1_total_income < 9000000:
        result = 'Kelas atas'
    else:
        result = 'Gaji tinggi banget'
    print(f'Pengecekan income {name} sebesar {income}, status = {result}')

check_income(customer1_name, customer1_total_income)
check_income(customer2_name, customer2_total_income)
check_income(customer3_name, customer3_total_income)
