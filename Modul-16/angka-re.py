# Mengambil semua angka dalam string
import re

text = "Nomor telepon saya adalah 08123456789 dan kode pos 12345"
pattern = r"\d+"

numbers = re.findall(pattern, text)
print("Angka ditemukan:", numbers)
