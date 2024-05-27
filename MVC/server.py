import socket
import psutil
import threading
import time
import queue


class Server:

    def __init__(self, connection_dict: dict):
        self.__connection_dict = connection_dict
        self.__server_running = False
        self.__device_name_callback = None
        self.__message_queue = queue.Queue()  # Queue for storing messages to be sent
        self.__client_sockets = []
        self.__init_ipv4_address()

    def __init_ipv4_address(self) -> None:
        __wifi_ip = None
        try:
            for addr in psutil.net_if_addrs()['Wi-Fi']:
                if addr.family == socket.AF_INET:
                    __wifi_ip = addr.address
                    break
        except (IndexError, KeyError) as e:
            print("Error:", e)
        self.__ip_address = __wifi_ip

    # Core
    def switch_on(self, port: int) -> str:
        if not self.__server_running:
            try:
                self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__server_socket.bind((self.__ip_address, int(port)))
                self.__server_socket.listen(3)
                self.__server_running = True

                # Thread to handle incoming connections
                connection_thread = threading.Thread(target=self.__handle_incoming_connection, daemon=True)
                connection_thread.start()
                # Thread to send messages to clients
                send_thread = threading.Thread(target=self.__send_messages_to_clients, daemon=True)
                send_thread.start()
                return 'Server nyala'
            
            except Exception as e:
                return str(e)
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
                return str(e)
        else:
            return 'Server belum nyala'

    def __handle_incoming_connection(self):
        while self.__server_running:
            try:
                client_socket, client_address = self.__server_socket.accept()
                self.__client_sockets.append(client_socket)
                client_thread = threading.Thread(target=self.__handle_clients, args=(client_socket, client_address), daemon=True)
                client_thread.start()  
            except OSError:
                break
            except Exception as e:
                print("Error:", e)

    def __handle_clients(self, client_socket, client_address):
        client_ip = client_address[0]
        device_name = self.__filtering_ip_client(ip_address_client=client_ip)
        if device_name:
            if self.__device_name_callback:
                self.__device_name_callback(device_name + ' [✔]')
            try:
                while self.__server_running:
                    data = client_socket.recv(1024)
                    if not data:
                        break
            except ConnectionAbortedError:
                pass
            except ConnectionResetError:
                if self.__device_name_callback:
                    self.__device_name_callback(device_name + ' [X]')
            finally:
                client_socket.close()
                if self.__device_name_callback:
                    self.__device_name_callback(device_name + ' [X]')
        else:
            client_socket.close()

    def __send_messages_to_clients(self):
        while self.__server_running:
            try:
                message = self.__message_queue.get(timeout=0.1)  # Get message from the queue
                for client_socket in self.__client_sockets:
                    try:
                        client_socket.send(message.encode())  # Send message to each client
                    except Exception as e:
                        print("Error sending message to client:", e)
            except queue.Empty:
                pass

    def __filtering_ip_client(self, ip_address_client) -> str:
        for device_name, ip_list in self.__connection_dict.items():
            if ip_address_client == ip_list:
                return device_name
        return None

    def set_device_name_callback(self, callback):
        self.__device_name_callback = callback
    
    def get_server_ip(self) -> str:
        return self.__ip_address
    
    def set_message(self, msg:str):
        self.__message_queue.put(msg)  # Put message into the queue