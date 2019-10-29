"""
OOP : Object Oriented Programing
OOP :
    - Encapsulation : membuat kelas yang terdiri dari variabel dan fungsi
    - Inheritance : encapsulation dari kelas yang sudah ada -> penurunan
    - Polymorphism : bentuk yang sama, akan beraksi berbeda tergantung kelas anaknya (inharitance)
"""
#Encapsulation
PRIA, WANITA = range(2)  # tipe data enumerasi, konstanta sebaiknya huruf besar tp ga wajib hanya sebaiknya
FIX, NON_FIX = range(2)


class Customer: #Cetakan untuk customer (class)
    def __init__(self, name, jenis_kelamin, total_income, existing, occupation, alamat):
        self.name = name
        self.jenis_kelamin = jenis_kelamin
        self.total_income = total_income
        self.existing = existing
        self.occupation = occupation
        self.alamat = alamat
    def __str__(self):
        return f'{self.name} bergaji {self.total_income}'

    def __repr__(self): #dibutuhkan tipe data string unicode
        return f'{self.name} bergaji {self.total_income}'

    def check_status_peminjaman(self):
        if self.existing:
            print(f'{self.name} masih aktif')
        else:
            print(f'{self.name} tidak aktif')

    def check_income(self):
        result = ''
        if self.total_income < 3000000:
            result = 'Gaji terlalu rendah'
        elif self.total_income >= 3000000 and self.total_income < 6000000:
            result = 'Kelas menengah'
        elif self.total_income >= 6000000 and self.total_income < 9000000:
            result = 'Kelas atas'
        else:
            result = 'Gaji tinggi banget'
        print(f'Pengecekan income {self.name} sebesar {self.total_income}, status = {result}')

#Proses mencetak customer (object)
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

customer1.check_status_peminjaman()
customer1.check_income()

#Inheritance dan Polymorphism
class BadCustomer(Customer) :
    def __str__(self):
        return f'BadCustomer {Customer.__str__(self)}'

    def __repr__(self):
        return f'BadCustomer {Customer.__str__(self)}'

customerX = BadCustomer('Boni', PRIA, 3500000, True, FIX,  {
    'Line 1': 'Kemanggisan',
    'Kelurahan': 'Setiabudi',
    'Kecamatan': 'Setiabudi',
    'City': 'Jakarta Selatan',
    'Provinsi': 'DKI Jakarta',
    'ZIP Code': '16444',
    'Country': 'Indonesia'
})
print (customerX)

