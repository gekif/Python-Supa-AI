# Latihan soal: Menampilkan waktu saat ini dan menambahkan durasi
from datetime import datetime, timedelta


def main():
    now = datetime.now()
    print("Waktu sekarang:", now.strftime("%d/%m/%Y %H:%M:%S"))

    # Tambah 1 minggu dan 2 jam
    future = now + timedelta(weeks=1, hours=2)
    print("Waktu setelah 1 minggu dan 2 jam:", future.strftime("%d/%m/%Y %H:%M:%S"))


if __name__ == "__main__":
    main()
