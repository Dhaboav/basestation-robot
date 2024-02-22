import socket
import threading


class Server:

    def __init__(self, connection_dict: dict):
            self.__host = socket.gethostbyname(socket.gethostname())
            self.__server_socket = None
            self.__running = False
            self.__list = connection_dict
            self.__socket_lock = threading.Lock()
            self.__device_tmp = None
            self.__device_name_callback = None

    def start(self, port: int) -> str:
        __response = None
        if not self.__running:
            try:
                # Create a new server socket
                self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__server_socket.bind((self.__host, int(port)))
                self.__server_socket.listen(3)
                self.__running = True
                __response = 'Hidup'

                server_thread = threading.Thread(target=self.__run_server)
                server_thread.start()
            except Exception as e:
                __response = e
                self.__running = False
        else:
            __response = 'Sudah hidup'
        return __response

    def __run_server(self):
        while self.__running:
            try:
                __client_socket, __addr = self.__server_socket.accept()
                __checking = self.__check_accepted_ip(__addr[0])
                
                print("Checking IP:", __addr[0], "Result:", __checking)
                print("Current Device:", self.__device_tmp)

                if __checking:
                    self.__device_name_callback(__checking)
                    # __client_thread = threading.Thread(target=self.__handle_client, args=(__client_socket,))
                    # __client_thread.start()

                    # Check client status immediately after accepting if IP is accepted
                    try:
                        __client_socket.settimeout(1)  # Set a timeout for recv
                        data = __client_socket.recv(1024)
                        if not data:
                            print("Client disconnected:", __addr)
                            __client_socket.close()
                        else:
                            print("Client still connected:", __addr)
                    except socket.timeout:
                        pass
                    except Exception as e:
                        print("Error checking client connection:", e)

                elif __checking != self.__device_tmp:
                    self.__device_tmp = __checking
                    self.__device_name_callback(__checking)
                    
                else:
                    print("Rejected!")
                    __client_socket.close()

            except Exception as e:
                print('Error accepting connection:', e)


    def shutdown(self):
        if self.__running:
            try:
                if self.__server_socket:
                    self.__server_socket.close()
                    self.__server_socket = None 
                    self.__running = False
                return 'Mati'
            except Exception as e:
                return e
        else:
            return 'Tidak hidup'


    # Getter
    def set_device_name_callback(self, callback):
        self.__device_name_callback = callback
    
    def get_server_ip(self) -> str:
        return self.__host
            
    # Other     
    def __check_accepted_ip(self, ip_address):
        for device_name, ip_list in self.__list.items():
            if ip_address in ip_list:
                return device_name
        return None