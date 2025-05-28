import queue
import threading


def worker(num, q):
    print(f"Thread menerima argumen: {num}")
    result = num * 2
    q.put(result)


q = queue.Queue()
thread = threading.Thread(target=worker, args=(5, q))
thread.start()
thread.join()

result = q.get()
print(f"Hasil dari thread: {result}")
