import requests


def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url, verify=False)  # Menonaktifkan verifikasi SSL
    if response.status_code == 200:
        data = response.json()
        return data['fact']
    else:
        return "Gagal mengambil data"


def get_random_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json()
        return data['message']  # URL gambar anjing
    else:
        return "Gagal mengambil data"


if __name__ == "__main__":
    print("Fakta Kucing:", get_cat_fact())
    print("Gambar Anjing Acak:", get_random_dog_image())
