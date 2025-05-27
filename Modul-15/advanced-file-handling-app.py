import json

try:
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(data)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    print("Periksa file JSON kamu, terutama karakter khusus atau format yang tidak valid.")
except FileNotFoundError:
    print("File 'data.json' tidak ditemukan. Pastikan file ada di direktori yang benar.")
except Exception as e:
    print(f"Terjadi error lain: {e}")
