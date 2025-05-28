# Mengganti semua spasi dengan underscore
import re

text = "Halo dunia Python"
pattern = r"\s+"

new_text = re.sub(pattern, "_", text)
print(new_text)  # Output: Halo_dunia_Python
