import threading


def worker():
    print("Worker thread berjalan")


thread = threading.Thread(target=worker)
thread.start()
thread.join()
