# import modul tkinter
import tkinter as tk

# Membuat jendela utama (Main Window)
root = tk.Tk()
root.title("Aplikasi Tkinter Pertamaku")
root.geometry("400x300") # Lebar x Tinggi dalam piksel


# Menambahkan widget

# Membuat label
label = tk.Label(root, text="Halo, Selamat Datang di Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # pack() untuk menampilkan widget, pady memberi jarak vertikal

# Membuat tombol
def tombol_ditekan():
    label.config(text="Tombol sudah ditekan!")

tombol = tk.Button(root, text="Klik Saya", command=tombol_ditekan)
tombol.pack()


# Menjalankan aplikasi
root.mainloop()

