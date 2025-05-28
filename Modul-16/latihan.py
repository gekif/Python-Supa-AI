# Validasi Email Sederhana
import re


def validasi_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


# Contoh Penggunaan
emails = ["user@example.com", "user.name@mail.co", "user@mail", "user@.com"]
for e in emails:
    print(f"{e}: {validasi_email(e)}")
