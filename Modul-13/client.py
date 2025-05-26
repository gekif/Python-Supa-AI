import socket


def start_client():
    # Membuat socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Koneksi ke server di localhost port 12345
    client_socket.connect(('localhost', 12345))

    # Kirim data ke server
    client_socket.sendall(b"Hello, Server")

    # Terima balasan dari server
    data = client_socket.recv(1024)
    print(f"Balasan dari server: {data.decode()}")

    # Tutup koneksi
    client_socket.close()


if __name__ == "__main__":
    start_client()
