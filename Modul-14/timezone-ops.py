# Zona waktu (timezone)
from datetime import datetime

import pytz

utc = pytz.utc
jakarta = pytz.timezone("Asia/Jakarta")

now_utc = datetime.now(utc)
now_jakarta = now_utc.astimezone(jakarta)

print("Waktu UTC:", now_jakarta)
print("Waktu Jakarta:", now_jakarta)
