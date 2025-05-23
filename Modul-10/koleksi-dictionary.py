# Membuat dictionary
mahasiswa = {
    "nama": "Andi",
    "umur": 21,
    "jurusan": "Informatika"
}

# Mengakses nilai berdasarkan key
print(mahasiswa["nama"]) # Output: Andi

# Menambahkan data baru
mahasiswa["semester"] = 5

# Menampilkan seluruh dictionary
for key, value in mahasiswa.items():
    print(f"{key}: {value}")