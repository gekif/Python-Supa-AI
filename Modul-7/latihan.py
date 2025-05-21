# Buat kelas Mobil dengan atribut merk, tahun, dan metode tampilkan_info() yang menampilkan informasi mobil.

class Mobil:
    def __init__(self, merk, tahun):
        self.__merk = merk  # Atribut privat
        self.__tahun = tahun  # Atribut privat

    def tampilkan_info(self):
        print(f"Merk: {self.__merk}")
        print(f"Tahun: {self.__tahun}")

    def set_merk(self, merk):
        self.__merk = merk

    def get_merk(self):
        return self.__merk
    

# Buat kelas MobilListrik yang mewarisi kelas Mobil dan tambahkan atribut kapasitas_baterai. Override metode tampilkan_info() untuk menampilkan info tambahan.

class MobilListrik(Mobil):
    def __init__(self, merk, tahun, kapasitas_baterai):
        super().__init__(merk, tahun)  # Memanggil konstruktor kelas induk
        self.__kapasitas_baterai = kapasitas_baterai  # Atribut privat

    def tampilkan_info(self):
        super().tampilkan_info()  # Memanggil metode kelas induk
        print(f"Kapasitas Baterai: {self.__kapasitas_baterai} kWh")


# Buat objek dari kedua kelas dan panggil metode tampilkan_info()
mobil1 = Mobil("Toyota", 2020)
mobil1.tampilkan_info()

mobil2 = MobilListrik("Tesla", 2021, 75)
mobil2.tampilkan_info()