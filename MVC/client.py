import socket


class Client:
    def __init__(self):
        self.__client_socket = None
        self.__connected = False

    def connect_to_server(self, ip:str, port:int):
        if not self.__connected:
            try:
                self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__client_socket.connect((ip, int(port)))
                self.__connected = True
                return 'Terhubung'
            except Exception as e:
                return e
        else:
            return 'Sudah terhubung'

    def disconnect_server(self):
        if self.__connected:
            try:
                self.__client_socket.close()
                self.__connected = False
                return 'Terputus'
            except Exception as e:
                return e
        else:
            return 'Tidak terhubung'