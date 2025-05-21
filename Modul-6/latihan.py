# Buat program yang membuka file bernama data.txt dan membaca isinya, lalu menampilkannya ke layar. Tangani exception jika file tidak ditemukan.

try:
    with open('data.txt', 'r') as file:
        isi = file.read()
        print(isi)
except FileNotFoundError:
    print("File 'data.txt' tidak ditemukan.")

#  Buat program yang menulis kalimat "Ini adalah baris pertama." ke dalam file output.txt. Jika file sudah ada, isinya akan ditimpa.
with open('output.txt', 'w') as file:
    file.write("Ini adalah baris pertama.\n")

# Buat program yang menambahkan kalimat "Baris tambahan." ke file output.txt tanpa menghapus isi sebelumnya.
with open('output.txt', 'a') as file:
    file.write("Baris tambahan.\n")