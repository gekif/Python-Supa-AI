# Operasi dengan timedelta
from datetime import datetime, timedelta

now = datetime.now()
print("Sekarang:", now)

# Tambah 7 hari
tambah_7_hari = now + timedelta(days=7)
print("7 hari kemudian:", tambah_7_hari)

# Kurangi 3 jam
kurangi_3_jam = now - timedelta(hours=3)
print("3 jam sebelumnya:", kurangi_3_jam)
