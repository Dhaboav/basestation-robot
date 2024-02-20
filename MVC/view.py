import tkinter as Tk

class View:
    def __init__(self, master, controller):
        self.__controller = controller
        self.__refbox_panel(master=master)
        self.__server_panel(master=master)
        self.__prompt_panel(master=master)
        
    

    def __refbox_panel(self, master):
        self.__refbox_label_frame = Tk.LabelFrame(master=master, text='REFBOX', width=200)
        self.__refbox_label_frame.grid(row=0, column=0, padx=10)
        # Component
        self.__label_ip_refbox = Tk.Label(master=self.__refbox_label_frame, text='IP')
        self.__ip_refbox = Tk.Entry(master=self.__refbox_label_frame, width=20)
        self.__label_port_refbox = Tk.Label(master=self.__refbox_label_frame, text='PORT')
        self.__port_refbox = Tk.Entry(master=self.__refbox_label_frame, width=20)
        self.__connect_button = Tk.Button(master=self.__refbox_label_frame, text='Connect', width=10, 
                                        foreground='white', background='green', command=self.set_connection_status)
        self.__disconnect_button = Tk.Button(master=self.__refbox_label_frame, text='Disconnect', width=10, 
                                        foreground='white', background='red', command=self.set_connection_statuss)
        self.__connection_status = Tk.Frame(master=self.__refbox_label_frame, width=25, height=25, background='red')
        # Position
        self.__label_ip_refbox.grid(row=0, column=0)
        self.__ip_refbox.grid(row=0, column=1, padx=(0, 10))
        self.__label_port_refbox.grid(row=1, column=0)
        self.__port_refbox.grid(row=1, column=1, padx=(0, 10), pady=10)
        self.__connect_button.grid(row=2, column=0, padx=(5, 5), pady=(5, 10), sticky="e")
        self.__disconnect_button.grid(row=2, column=1, padx=(5, 0), pady=(5, 10), sticky="w")
        self.__connection_status.grid(row=2, column=1, padx=(100, 0), pady=(5, 10), sticky="w")

    def __server_panel(self, master):
        self.__server_label_frame = Tk.LabelFrame(master=master, text='SERVER', width=200)
        self.__server_label_frame.grid(row=1, column=0, padx=10)
        # Component
        self.__label_port_server = Tk.Label(master=self.__server_label_frame, text='PORT')
        self.__port_server = Tk.Entry(master=self.__server_label_frame, width=20)
        self.__connect_server_button = Tk.Button(master=self.__server_label_frame, text='Connect', width=10, 
                                        foreground='white', background='green', command=self.set_connection_status)
        self.__disconnect_server_button = Tk.Button(master=self.__server_label_frame, text='Disconnect', width=10, 
                                        foreground='white', background='red', command=self.set_connection_statuss)
        self.__server_status = Tk.Frame(master=self.__server_label_frame, width=25, height=25, background='red')
        # Position
        self.__label_port_server.grid(row=0, column=0)
        self.__port_server.grid(row=0, column=1, padx=(0, 10))
        self.__connect_server_button.grid(row=2, column=0, padx=(5, 5), pady=10, sticky="e")
        self.__disconnect_server_button.grid(row=2, column=1, padx=(5, 0), pady=10, sticky="w")
        self.__server_status.grid(row=2, column=1, padx=(100, 0), pady=10, sticky="w")

    def __prompt_panel(self, master):
        self.__prompt_label_frame = Tk.LabelFrame(master=master, text='PROMPT', width=200)
        self.__prompt_label_frame.grid(row=2, column=0, padx=10)
        # Componenet
        self.__text_area = Tk.Text(master=self.__prompt_label_frame, width=25, height=10, 
                                   foreground='chartreuse1', background='black', font=('Consolas', 11))
        self.__clear_button = Tk.Button(master=self.__prompt_label_frame, text='Clear', width=10, 
                                        foreground='white', background='blue', command=self.__controller.clear_prompt)
        # Position
        self.__text_area.grid(row=0, column=0, padx=10, pady=5)
        self.__clear_button.grid(row=1, column=0, pady=(5,10))
    

    def set_empty_text_area(self):
        self.__text_area.delete('1.0', Tk.END)

    def set_connection_status(self):
        self.__server_status.config(background='green')
    
    def set_connection_statuss(self):
        self.__server_status.config(background='red')
        