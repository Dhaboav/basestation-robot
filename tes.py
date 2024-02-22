import socket

def simple_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to server.")

    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print("Received message from server:", message)
    except Exception as e:
        client_socket.close()
        print(f"Error receiving message: {e}")

    print("Closing connection.")
    client_socket.close()

if __name__ == "__main__":
    HOST = '192.168.56.1'  # Server's IP address or hostname
    PORT = 123       # Server's port
    simple_client(HOST, PORT)
