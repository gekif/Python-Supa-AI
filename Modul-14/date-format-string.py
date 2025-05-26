# Format dan parsing tanggal waktu - format tanggal ke string
from datetime import datetime

now = datetime.now()
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted datetime:", formatted)
