import requests

url = "https://catfact.ninja/fact"
response = requests.get(url, verify=False)  # Menonaktifkan verifikasi SSL

if response.status_code == 200:
    data = response.json()
    print("Fakta Kucing:", data['fact'])
else:
    print("Gagal mengambil data")
