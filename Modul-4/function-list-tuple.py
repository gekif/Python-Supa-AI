# Fungsi (Function) di Python

def sapa():
    print("Halo, selamat datang")

sapa()



# Fungsi dengan Parameter dan Return Value

def tambah(a, b):
    return a + b

hasil = tambah(3, 4)
print(hasil)  # Output: 7



# List

buah = ["apel", "jeruk", "pisang"]

print(buah[1])  # Output: jeruk

# Mengubah elemen dalam list
buah.append("mangga")

print(buah)  # Output: ['apel', 'jeruk', 'pisang', 'mangga']



# Tuple

koordinat = (10, 20)

print(koordinat[0])  # Output: 10