# Membuat kelas dan objek di Python

# Membuat kelas bernama Mahasiswa
class Mahasiswa:
    # Konstruktor untuk inisialisasi atribut
    def __init__(self, nama, umur, jurusan):
        self.nama = nama  # Atribut nama
        self.umur = umur  # Atribut umur
        self.jurusan = jurusan  # Atribut jurusan

    # Metode untuk menampilkan info mahasiswa
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
        print(f"Jurusan: {self.jurusan}")


# Membuat objek dari kelas Mahasiswa
mhs1 = Mahasiswa("Andi", 21, "Informatika")


# Memanggil metode objek
mhs1.tampilkan_info()



#  Inheritance
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Suara hewan")


# Kelas anak yang mewarisi kelas Hewan
class Anjing(Hewan):
    def suara(self):
        print("Guk guk")


# Membuat objek Anjing
anjing1 = Anjing("Buddy")
anjing1.suara()  # Output: Guk guk



# Polymorphism
class Kucing(Hewan):
    def suara(self):
        print("Meong")

hewan_list = [Anjing("Buddy"), Kucing("Kitty")]

for hewan in hewan_list:
    hewan.suara()  # Output: Guk guk, Meong



# Encapsulation
class BankAccount:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atribut privat

    def deposit(self, jumlah):
        self.__saldo += jumlah

    def get_saldo(self):
        return self.__saldo
    

rekening = BankAccount(1000)
rekening.deposit(500)

print(rekening.get_saldo())  # Output: 1500