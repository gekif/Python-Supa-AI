# Membuat set
angka = {1, 2, 3, 4, 5}

# Menambah elemen
angka.add(6)

# Menghapus elemen
angka.remove(3)

# Operasi himpunan
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a.union(set_b)) # {1, 2, 3, 4, 5}
print(set_a.intersection(set_b)) # {3}
print(set_a.difference(set_b)) # {1, 2}
print(set_b.difference(set_a)) # {4, 5}