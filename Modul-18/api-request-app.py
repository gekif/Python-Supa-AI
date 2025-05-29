import requests
from requests.exceptions import SSLError, RequestException

url = "https://catfact.ninja/fact"  # Contoh API yang memberikan fakta kucing

try:
    # Menonaktifkan verifikasi SSL dengan verify=False
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()
        print("Data dari API:", data)
    else:
        print(f"Gagal mengambil data dari API, status code: {response.status_code}")

except SSLError as ssl_err:
    print("Terjadi error SSL:", ssl_err)
except RequestException as req_err:
    print("Terjadi error saat request:", req_err)
