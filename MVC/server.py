import socket
import threading


class Server:

    def __init__(self, connection_dict: dict):
            self.__ip_address = socket.gethostbyname(socket.gethostname())
            self.__connection_dict = connection_dict
            self.__server_running = False
            self.__device_name_callback = None

    # Core
    def switch_on(self, port: int) -> str:
        if not self.__server_running:
            try:
                self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__server_socket.bind((self.__ip_address, int(port)))
                self.__server_socket.listen(3)

                self.__server_running = True

                # Thread untuk handle koneksi masuk
                connection_thread = threading.Thread(target=self.__handle__incoming_connection, daemon=True)
                connection_thread.start()
                return 'Server nyala'
            
            except Exception as e:
                return e
        else:
            return 'Server sudah nyala'
        
    def switch_off(self):
        if self.__server_running:
            try:
                self.__server_socket.close()
                self.__server_running = False
                return 'Server mati'
            except Exception as e:
                return e
        else:
            return 'Server belum nyala'

    def __handle__incoming_connection(self):
        while self.__server_running:
            try:
                print('Cps')
                if self.__server_socket is None:
                    print('oerh')
                    break
                __client_socket, __client_address = self.__server_socket.accept()
                __client_thread = threading.Thread(target=self.__handle_clients, args=(__client_socket, __client_address))
                __client_thread.start()  
            except OSError as i:
                print(f'OS: {i}')
                break
            except Exception as e:
                print(f'Unexpected error: {e}')
                break
        print('Exiting __handle__incoming_connection')

    def __handle_clients(self, client_socket, client_address):
        __client_ip = client_address[0]
        __device_name = self.__filtering_ip_client(ip_address_client=__client_ip)
        if __device_name:
            if self.__device_name_callback:
                self.__device_name_callback(__device_name + ' Tersambung')

            send_thread = threading.Thread(target=self.send_messages, args=(client_socket, __device_name))
            send_thread.start()

                # Nerima data dari client:
            # try:
            #     # Create a new thread to send messages
            #     # Handle receiving data from the client
            #     while True:
            #         data = client_socket.recv(1024)
            #         if not data:
            #             break
            #         print(f"Received data from {__device_name}: {data.decode()}")

            # except ConnectionResetError:
            #     if self.__device_name_callback:
            #         self.__device_name_callback(__device_name + ' Terputus')
            # finally:
            #     client_socket.close()
        else:
            pass
            client_socket.close()

    def send_messages(self, client_socket, device_name):
        while self.__server_running:
            # Check if the client socket is still open
            if client_socket.fileno() == -1:
                print(f"Client socket for {device_name} is closed. Stopping send thread.")
                break

            # Send a message to the client
            message = f"Hello from server to {device_name}"
            try:
                client_socket.send(message.encode())
                print(f"Sent message to {device_name}: {message}")
            except ConnectionResetError:
                if self.__device_name_callback:
                    self.__device_name_callback(device_name + ' Terputus')
                break



    # Other     
    def __filtering_ip_client(self, ip_address_client) -> str:
        for device_name, ip_list in self.__connection_dict.items():
            if ip_address_client in ip_list:
                return device_name
        return None

    # Getter
    def set_device_name_callback(self, callback):
        self.__device_name_callback = callback
    
    def get_server_ip(self) -> str:
        return self.__ip_address