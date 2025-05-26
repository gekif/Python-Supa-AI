# Membuat objek tanggal dan waktu manual
from datetime import datetime, date, time

# Membuat tanggal
tanggal = date(2025, 5, 26)
print("Tanggal", tanggal)

# Membuat waktu
waktu = time(14, 30, 1)
print("Waktu", waktu)

# Membuat datetime
dt = datetime(2025, 5, 26, 14, 30, 1)
print("Datetime", dt)
