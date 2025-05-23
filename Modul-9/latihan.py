# Membuat dictionary untuk menyimpan data buku (judul, penulis, tahun terbit).
buku = {
    "judul": "Belajar Python",
    "penulis": "John Doe",
    "tahun_terbit": 2023
}

# Menampilkan data buku
print("Data Buku:")
print("Judul:", buku["judul"])
print("Penulis:", buku["penulis"])
print("Tahun Terbit:", buku["tahun_terbit"])


# Membuat set untuk menyimpan genre buku tanpa duplikat
genre_buku = {"Fiksi", "Non-Fiksi", "Teknologi"}

# Menambahkan genre baru
genre_buku.add("Sains")

# Menampilkan isi set genre buku
print("Genre Buku:")
for genre in genre_buku:
    print("-", genre)


# Menambahkan data baru dan menampilkan isi dictionary dan set.
buku["penerbit"] = "Penerbit ABC"

print("\nData Buku Setelah Penambahan:")

# Cara 1: Menggunakan kunci untuk mengakses nilai
'''
print("Judul:", buku["judul"])
print("Penulis:", buku["penulis"])
print("Tahun Terbit:", buku["tahun_terbit"])
print("Penerbit:", buku["penerbit"])
'''

# Cara 2: Menggunakan loop untuk menampilkan semua data
for key, value in buku.items():
    print(f"{key.capitalize()}: {value}")