import socket


def start_server():
    # Membuat socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket ke alamat dan port
    server_socket.bind(('localhost', 12345))

    # Listen koneksi masuk, maksimal 1 antrian
    server_socket.listen(1)
    print("Server siap menerima koneksi di port 12345...")

    # Terima koneksi dari client
    conn, addr = server_socket.accept()
    print(f"Terhudung dengan {addr}")

    # Terima data dari client
    data = conn.recv(1024)
    print(f"Data diterima dari client: {data.decode()}")

    # Kirim balasan ke client
    conn.sendall(b"Pesan diterima oleh server")

    # Tutup koneksi
    conn.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()
