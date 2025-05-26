# Format dan parsing tanggal waktu - parsing string ke tanggal
from datetime import datetime

tanggal_str = "26-05-2025 14:30:15"
tanggal_obj = datetime.strptime(tanggal_str, "%d-%m-%Y %H:%M:%S")
print("Objek datetime:", tanggal_obj)
