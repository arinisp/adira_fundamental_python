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

    def cari_motor_yang_sesuai(self):
        result = ''
    if self.total_income < 3000000:
        result = 'Beat'
    elif self.total_income >= 3000000 and self.total_income < 6000000:
        result = 'Vario'
    else:
        result = 'N-Max'
    print(f'Motor yang sesuai untuk {self.total_income} adalah {result}')