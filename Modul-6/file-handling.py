# Membuka file dengan mode 'w' (write) untuk menulis isi baru ke file
# Jika file belum ada, maka file akan dibuat
with open('contoh.txt', 'w') as file:
    # Menulis string ke dalam file
    file.write("Hallo, ini adalah baris pertama.\n")
    file.write("Ini adalah baris kedua.\n")
# File otomatis tertutup setelah keluar dari blok with

# Membuka file dengan mode 'a' (append) untuk menambahkan isi tanpa menghapus isi lama
with open('contoh.txt', 'a') as file:
    # Menambahkan baris baru ke file
    file.write("Ini adalah baris tambahan.\n")

# Membuka file dengan mode 'r' (read) untuk membaca isi file
try:
    with open('contoh.txt', 'r') as file:
        # Membaca seluruh isi file sebagai string
        isi_file = file.read()
        # Menampilkan isi file ke layar
        print("Isi file 'contoh.txt':")
        print(isi_file)
except FileNotFoundError:
    # Menangani jika file tidak ditemukan
    print("File 'contoh.txt' tidak ditemukan.")

# Contoh penggunaan mode 'x' untuk membuat file baru
# Jika file sudah ada, maka akan menimbulkan error FileExistsError
try:
    with open('file_baru.txt', 'x') as file:
        file.write("Ini adalah file baru yang dibuat dengan mode 'x'.\n")
    print("File 'file_baru.txt' berhasil dibuat.")
except FileExistsError:
    print("File 'file_baru.txt' sudah ada, tidak bisa membuat file baru dengan mode 'x'.")

# Contoh menutup file secara manual (tidak menggunakan 'with')
file_manual = open('contoh.txt', 'w') # mmembuka file untuk menulis
file_manual.write("Ini contoh menulis file tanpa 'with'.\n")
file_manual.close() # Penting untuk menutup file agar data tersimpan dengan benar