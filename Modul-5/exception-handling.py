# Try and Except

try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")


# Menangani Beberapa Exception

try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")
except ValueError:
    print("Input harus berupa angka!")
finally:
    print("Program selesai.")
