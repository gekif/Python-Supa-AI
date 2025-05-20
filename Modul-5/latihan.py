# Buat program yang meminta input angka dari pengguna dan membagi 100 dengan angka tersebut. Tangani exception jika pengguna memasukkan nol atau bukan angka

try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")
except ValueError:
    print("Input harus berupa angka!")
finally:
    print("Program selesai.")


# Buat contoh kode yang menggunakan blok try, except, dan else

try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!") 
else:
    print(f"Hasil pembagian 100 dengan {angka} adalah {hasil}")