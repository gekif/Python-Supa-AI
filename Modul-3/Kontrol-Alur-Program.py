# Pernyataan kondisional

angka = 5 # Angka positif

if angka > 0:
    print("Angka positif")
elif angka == 0:
    print("Angka nol")
else:
    print("Angka negatif")


# Operator Perbandingan dan Logika

if angka > 0 and angka % 2 == 0:
    print("Angka positif genap")
else:
    print("Angka positif ganjil")


#  Looping - For 

for huruf in "Python":
    print(huruf) # Mengulangi setiap huruf dalam string "Python" 


# Looping - While

hitung = 5

while hitung > 0:
    print(hitung) # Cetak nilai hitung => 5
    hitung -= 1 # sama dengan hitung = hitung - 1, tercetak 4, 3, 2, 1


# Penggunaan break

for i in range(10):
    if i == 5:
        break # Menghentikan loop saat i sama dengan 5
    print(i) # Cetak nilai i => 0, 1, 2, 3, 4
