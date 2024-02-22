import socket
import threading
import time


class Server:

    def __init__(self, connection_dict: dict):
            self.__ip_address = socket.gethostbyname(socket.gethostname())
            self.__connection_dict = connection_dict
            self.__server_running = False
            self.__device_name_callback = None
            self.__message = 'Tersambung'
            self.__client_sockets = []

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
                self.__server_running = False
                self.__server_socket.close()
                # Close all client sockets
                for client_socket in self.__client_sockets:
                    client_socket.close()

                return 'Server mati'
            except Exception as e:
                return e
        else:
            return 'Server belum nyala'

    def __handle__incoming_connection(self):
        while self.__server_running:
            try:
                __client_socket, __client_address = self.__server_socket.accept()
                self.__client_sockets.append(__client_socket)
                __client_thread = threading.Thread(target=self.__handle_clients, args=(__client_socket, __client_address))
                __client_thread.start()  
            except OSError:
                break
            except Exception:
                break

    def __handle_clients(self, client_socket, client_address):
        __client_ip = client_address[0]
        __device_name = self.__filtering_ip_client(ip_address_client=__client_ip)
        if __device_name:
            if self.__device_name_callback:
                self.__device_name_callback(__device_name + ' Tersambung')

            send_thread = threading.Thread(target=self.__server_to_client, args=(client_socket, __device_name))
            send_thread.start()

            # Nerima data dari client:
            try:
                while self.__server_running:
                    data = client_socket.recv(1024)
                    if not data:
                        break
            except ConnectionAbortedError:
                pass
            except ConnectionResetError:
                if self.__device_name_callback:
                    self.__device_name_callback(__device_name + ' Terputus')
            finally:
                client_socket.close()
        else:
            pass
            client_socket.close()

    def __server_to_client(self, client_socket, device_name):
        while self.__server_running:
            # Check if the client socket is still open
            if client_socket.fileno() == -1:
                break
            try:
                if self.__message:
                    client_socket.send(self.__message.encode())
                    self.__message = None
                else:
                    time.sleep(0.1)
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
    
    def set_messeage(self, msg:str):
        self.__message = msg