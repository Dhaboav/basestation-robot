import tkinter as Tk


class View:
    def __init__(self, master, controller):
        self.__controller = controller

        # Refbox
        self.__connect_frame = Tk.LabelFrame(master=master, text='REFBOX')
        self.__connect_frame.grid(row=0, column=0, padx=10)

        # Component
        self.__label_ip_refbox = Tk.Label(master=self.__connect_frame, text='IP')
        self.__ip_refbox = Tk.Entry(master=self.__connect_frame, width=20)
        self.__label_port_refbox = Tk.Label(master=self.__connect_frame, text='PORT')
        self.__port_refbox = Tk.Entry(master=self.__connect_frame, width=20)
        self.__connect_button = Tk.Button(master=self.__connect_frame, text='Connect', width=10, 
                                        foreground='white', background='green', command=self.set_connection_status)
        self.__disconnect_button = Tk.Button(master=self.__connect_frame, text='Disconnect', width=10, 
                                        foreground='white', background='red', command=self.set_connection_statuss)
        self.__connection_status = Tk.Frame(master=self.__connect_frame, width=25, height=25, background='red')

        # Position
        self.__label_ip_refbox.grid(row=0, column=0)
        self.__ip_refbox.grid(row=0, column=1, padx=(0, 10))
        self.__label_port_refbox.grid(row=1, column=0)
        self.__port_refbox.grid(row=1, column=1, padx=(0, 10), pady=10)
        self.__connect_button.grid(row=2, column=0, padx=(5, 5), pady=(5, 10), sticky="e")
        self.__disconnect_button.grid(row=2, column=1, padx=(5, 0), pady=(5, 10), sticky="w")
        self.__connection_status.grid(row=2, column=1, padx=(100, 0), pady=(5, 10), sticky="w")

    def set_connection_status(self):
        self.__connection_status.config(background='green')
    
    def set_connection_statuss(self):
        self.__connection_status.config(background='red')
        