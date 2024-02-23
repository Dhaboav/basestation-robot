from MVC.model import Model
from MVC.view import View
from MVC.client import Client
from MVC.server import Server


class Controller:
    def __init__(self, master):
        self.__model = Model()
        self.__view = View(master=master, controller=self)
        self.__client = Client()
        self.__client.set_message_callback(callback=self.handle_received_message)
        self.__server = Server(self.__model.get_ip_address())
        self.__server.set_device_name_callback(callback=self.handle_device_connection)
        self.__status_server = False
        self.__status_client = False

    def connect_refbox(self):
        __ip_refbox = self.__view.get_ip_refbox()
        __port_refbox = self.__view.get_port_refbox()
        __connecting = self.__client.connect_to_server(ip=__ip_refbox, port=__port_refbox)
        if __connecting == 'Terhubung':
            self.__view.set_connection_status_connected()
            self.__view.set_prompt_log(message=__connecting + ' Refbox')
            self.__status_client = True
            self.__client.start_receiving()
        elif __connecting == 'Sudah terhubung':
            self.__view.show_info_dialog(title='Connection Info', message=__connecting + ' ke refbox')
        else:
            self.__view.show_error_dialog(title='Connection Error', message=__connecting)

    def disconnect_refbox(self):
        __connecting = self.__client.disconnect_server()
        if __connecting == 'Terputus':
            self.__view.set_connection_status_disconnect()
            self.__view.set_prompt_log(message=__connecting + ' Refbox')
            self.__status_client = False
        elif __connecting == 'Tidak terhubung':
            self.__view.show_info_dialog(title='Connection Info', message= __connecting + ' ke refbox')
        else:
            self.__view.show_error_dialog(title='Connection Error', message=__connecting)

    def server_online(self):
        __port = self.__view.get_port_server()
        __basestation = self.__server.switch_on(port=__port)
        if __basestation == 'Server nyala':
            __ip_address = self.__server.get_server_ip()
            self.__view.set_server_status_on()
            self.__view.set_server_ip(IP_server=__ip_address)
            self.__view.set_prompt_log(message=__basestation)
            self.__status_server = True
        elif __basestation == 'Server sudah nyala':
            self.__view.show_info_dialog(title='Connection Info', message=__basestation)
        else:
            self.__view.show_error_dialog(title='Connection Error', message=__basestation)

    def server_offline(self):
        __basestation = self.__server.switch_off()
        if __basestation == 'Server mati':
            self.__view.set_server_status_off()
            self.__view.set_server_ip(IP_server='')
            self.__view.set_prompt_log(message=__basestation)
            self.__status_server = False
        elif __basestation == 'Server belum nyala':
            self.__view.show_info_dialog(title='Connection Info', message=__basestation)
        else:
            self.__view.show_error_dialog(title='Connection Error', message=__basestation)

    def clear_prompt(self):
        self.__view.set_empty_text_area()

    def handle_received_message(self, message:str):
        if message == 'Koneksi terputus':
            self.__view.set_connection_status_disconnect()
            self.__view.set_prompt_log(message=message)
            self.__view.show_error_dialog(title='Connection Error', message='Koneksi ke Refbox Terputus')
        else:
            __translated = self.__model.get_refbox_message_dict(key=message)
            if self.__status_server and self.__status_client:
                if __translated is not None:
                    __check = self.__model.get_keep_character(key=message)
                    self.__server.set_message(msg=__check)
                    self.__view.set_prompt_log(message=__translated)
                else:
                    self.__view.set_prompt_log(message=message)
            else:
                if __translated is not None:
                    self.__view.set_prompt_log(message=__translated)
                else:
                    self.__view.set_prompt_log(message=message)

    def handle_device_connection(self, message:str):
        self.__view.set_prompt_log(message=message)

    def handle_control_button(self, button_id:str) -> str:
        __button2robot = self.__model.get_button_dict(key=button_id)
        self.__server.set_message(msg=__button2robot)
        self.__view.set_prompt_log(message=button_id)     