# Download File dengan Threading
import threading

import requests


def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"{filename} selesai di-download")


urls = [
    ("https://example.com/file1.jpg", "file1.jpg"),
    ("https://example.com/file2.jpg", "file2.jpg")
]

threads = []
for url, filename in urls:
    t = threading.Thread(target=download_file, args=(url, filename))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Semua file selesai di-download")
