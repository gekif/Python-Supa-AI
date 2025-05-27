from multiprocessing import Process


def worker():
    print("Worker process berjalan")


if __name__ == "__main__":
    process = Process(target=worker)
    process.start()
    process.join()
