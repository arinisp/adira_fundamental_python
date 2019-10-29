from database.customer import Customer

PRIA, WANITA = range(2)  # tipe data enumerasi, konstanta sebaiknya huruf besar tp ga wajib hanya sebaiknya
FIX, NON_FIX = range(2)

customer1 = Customer('Boni', PRIA, 3500000, True, FIX,  {
    'Line 1': 'Kemanggisan',
    'Kelurahan': 'Setiabudi',
    'Kecamatan': 'Setiabudi',
    'City': 'Jakarta Selatan',
    'Provinsi': 'DKI Jakarta',
    'ZIP Code': '16444',
    'Country': 'Indonesia'
})
customer2 = Customer('Sari', WANITA, 5500000, False, FIX, {})
customer3 = Customer('Eka', WANITA,10000000, True, NON_FIX, {})

print(customer1)
print(customer2)
print(customer3)