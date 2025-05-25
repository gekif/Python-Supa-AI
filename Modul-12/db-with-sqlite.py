import sqlite3

# Membuat koneksi ke database SQLite (file database.db)
conn = sqlite3.connect('database.db')

# Membuat cursor untuk eksekusi query
cursor = conn.cursor()

# Membuat tabel
cursor.execute('''
INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (?, ?, ?)
''', ('Belajar Python', 'John Doe', 2023))

# Commit perubahan
conn.commit()


# Mengambil data
cursor.execute('SELECT * FROM buku')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Menutup koneksi
conn.close()