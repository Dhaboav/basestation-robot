from MVC.model import Model
from MVC.view import View
from MVC.client import Client


class Controller:
    def __init__(self, master):
        self.__model = Model()
        self.__view = View(master=master, controller=self)
        self.__client = Client()

    def connect_refbox(self):
        __ip_refbox = self.__view.get_ip_refbox()
        __port_refbox = self.__view.get_port_refbox()
        __connecting = self.__client.connect_to_server(ip=__ip_refbox, port=__port_refbox)
        if __connecting == 'Terhubung':
            self.__view.set_connection_status_connected()
            self.__view.set_prompt_log(__connecting + ' Refbox')
        elif __connecting == 'Sudah terhubung':
            self.__view.show_info_dialog('Connection Info', __connecting + ' ke refbox')
        else:
            self.__view.show_error_dialog('Connection Error', __connecting)

    def disconnect_refbox(self):
        __connecting = self.__client.disconnect_server()
        if __connecting == 'Terputus':
            self.__view.set_connection_status_disconnect()
            self.__view.set_prompt_log(__connecting + ' Refbox')
        elif __connecting == 'Tidak terhubung':
            self.__view.show_info_dialog('Connection Info', __connecting + ' ke refbox')
        else:
            self.__view.show_error_dialog('Connection Error', __connecting)

    def clear_prompt(self):
        self.__view.set_empty_text_area()