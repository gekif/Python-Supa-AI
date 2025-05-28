import threading
import time


def worker():
    print(f"Thread {threading.current_thread().name} mulai bekerja")
    time.sleep(2)
    print(f"Thread {threading.current_thread().name} selesai bekerja")


# Membuat thread
thread1 = threading.Thread(target=worker, name='Worker-1')
thread2 = threading.Thread(target=worker, name='Worker-2')

# Memulai thread
thread1.start()
thread2.start()

# Menunggu thread selesai
thread1.join()
thread2.join()
