import socket
import threading


class Client:
    def __init__(self):
        self.__client_socket = None
        self.__connected = False
        self.__message_callback = None

    def connect_to_server(self, ip: str, port: int):
        if not self.__connected:
            try:
                self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__client_socket.settimeout(2.0)
                self.__client_socket.connect((ip, int(port)))
                self.__connected = True
                self.__client_socket.settimeout(None)
                return 'Terhubung'
            except socket.timeout:
                self.__client_socket.close()
                self.__client_socket = None
                return 'Tidak dapat terhubung'
            except ValueError:
                return 'PORT harus angka'
            except Exception as e:
                return e
        else:
            return 'Sudah terhubung'

    def disconnect_server(self):
        if self.__connected:
            try:
                self.__client_socket.close()
                self.__client_socket = None
                self.__connected = False
                return 'Terputus'
            except Exception as e:
                return e
        else:
            return 'Tidak terhubung'
        
    def __receive_data(self):
        try:
            while self.__connected:
                data = self.__client_socket.recv(1024)
                if not data:
                    self.handle_disconnect()
                    break
                if self.__message_callback:
                    self.__message_callback(data.decode('utf-8'))
        except ConnectionAbortedError as i:
            pass
        except socket.error:
            self.handle_disconnect()
            
    def start_receiving(self):
        start_thread = threading.Thread(target=self.__receive_data)
        start_thread.daemon = True
        start_thread.start()

    def set_message_callback(self, callback):
        self.__message_callback = callback
    
    def handle_disconnect(self):
        self.disconnect_server()
        if self.__message_callback:
            self.__message_callback('Koneksi terputus')