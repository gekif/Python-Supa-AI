# Mencari pola di awal string
import re

text = "Halo dunia"
pattern = r"^Halo"

match = re.match(pattern, text)
if match:
    print("Cocok", match.group())
else:
    print("Tidak cocok")
