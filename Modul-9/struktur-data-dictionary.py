# Membuat Dictionary
data_mahasiswa = {
    "nama": "Andi",
    "umur": 21,
    "jurusan": "Informatika"
}

# Mengakses value
print(data_mahasiswa["nama"]) # Output: Andi

# Menambah item baru
data_mahasiswa["semester"] = 5

# Mengubah value
data_mahasiswa["umur"] = 22

# Menghapus item
del data_mahasiswa["jurusan"]

# Iterasi Dictionary
for key, value in data_mahasiswa.items():
    print(f"{key}: {value}")