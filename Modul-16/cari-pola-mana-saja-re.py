# Mencari pola di mana saja dalam string
import re

text = "Saya suka belajar Python"
pattern = r"belajar"

search = re.search(pattern, text)
if search:
    print("Ditemukan:", search.group())
else:
    print("Tidak ditemukan")
