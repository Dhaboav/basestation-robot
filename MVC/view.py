import tkinter as Tk
import tkinter.font as font


class View:
    def __init__(self, master, controller):
        self.__controller = controller
        self.__refbox_panel(master=master)
        self.__server_panel(master=master)
        self.__prompt_panel(master=master)
        self.__team_panel(master=master)
        self.__control_panel(master=master)

    def __refbox_panel(self, master):
        self.__refbox_label_frame = Tk.LabelFrame(master=master, text='REFBOX', width=200)
        self.__refbox_label_frame.grid(row=0, column=0, padx=(5, 0))
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
        self.__label_ip_server = Tk.Label(master=self.__server_label_frame, text='IP')
        self.__server_ip = Tk.Label(master=self.__server_label_frame, text='', foreground='green')
        self.__label_port_server = Tk.Label(master=self.__server_label_frame, text='PORT')
        self.__port_server = Tk.Entry(master=self.__server_label_frame, width=20)
        self.__connect_server_button = Tk.Button(master=self.__server_label_frame, text='Connect', width=10, 
                                        foreground='white', background='green', command=self.set_connection_status)
        self.__disconnect_server_button = Tk.Button(master=self.__server_label_frame, text='Disconnect', width=10, 
                                        foreground='white', background='red', command=self.set_connection_statuss)
        self.__server_status = Tk.Frame(master=self.__server_label_frame, width=25, height=25, background='red')
        # Position
        self.__label_ip_server.grid(row=0, column=0)
        self.__server_ip.grid(row=0, column=1)
        self.__label_port_server.grid(row=1, column=0)
        self.__port_server.grid(row=1, column=1, padx=(0, 10))
        self.__connect_server_button.grid(row=2, column=0, padx=(5, 5), pady=10, sticky="e")
        self.__disconnect_server_button.grid(row=2, column=1, padx=(5, 0), pady=10, sticky="w")
        self.__server_status.grid(row=2, column=1, padx=(100, 0), pady=10, sticky="w")

    def __prompt_panel(self, master):
        self.__prompt_label_frame = Tk.LabelFrame(master=master, text='PROMPT', width=200)
        self.__prompt_label_frame.grid(row=2, column=0, padx=10)
        # Component
        self.__text_area = Tk.Text(master=self.__prompt_label_frame, width=25, height=9, 
                                   foreground='chartreuse1', background='black', font=('Consolas', 11))
        self.__clear_button = Tk.Button(master=self.__prompt_label_frame, text='Clear', width=10, 
                                        foreground='white', background='blue', command=self.__controller.clear_prompt)
        # Position
        self.__text_area.grid(row=0, column=0, padx=10, pady=5)
        self.__clear_button.grid(row=1, column=0, pady=(5,10))

    def __team_panel(self, master):
        self.__team_label_frame = Tk.LabelFrame(master=master, text='TEAM INDICATOR', width=200)
        self.__team_label_frame.grid(row=0, column=1)
        # Component
        self.__team_name = Tk.Label(master=self.__team_label_frame, text='Unknown')
        self.__color_team_tag = Tk.Frame(master=self.__team_label_frame, width=50, height=25, background='black')
        # Position
        self.__team_name.pack(side='left')
        self.__color_team_tag.pack(side='right')

    def __control_panel(self, master):
        self.__control_label_frame = Tk.LabelFrame(master=master, text='CONTROL PANEL', width=200)
        self.__control_label_frame.grid(row=1, rowspan=3, column=1)
        self.__control_font = font.Font(family='Calibri', size=16, weight='bold')
        # Component
        self.__kickoff_button = Tk.Button(master=self.__control_label_frame, text='K | kick off', width=10, 
                                        foreground='white', background='blue')
        self.__kickoff_button['font'] = self.__control_font
        self.__freekick_button = Tk.Button(master=self.__control_label_frame, text='F | free kick', width=10, 
                                        foreground='white', background='blue')
        self.__freekick_button['font'] = self.__control_font
        self.__goalkick_button = Tk.Button(master=self.__control_label_frame, text='G | goal kick', width=10, 
                                        foreground='white', background='blue')
        self.__goalkick_button['font'] = self.__control_font
        self.__throwin_button = Tk.Button(master=self.__control_label_frame, text='T | throw in', width=10, 
                                        foreground='white', background='blue')
        self.__throwin_button['font'] = self.__control_font
        self.__corner_button = Tk.Button(master=self.__control_label_frame, text='C | corner', width=10, 
                                        foreground='white', background='blue')
        self.__corner_button['font'] = self.__control_font
        self.__penalty_button = Tk.Button(master=self.__control_label_frame, text='P | penalty', width=10, 
                                        foreground='white', background='blue')
        self.__penalty_button['font'] = self.__control_font
        self.__repair_button = Tk.Button(master=self.__control_label_frame, text='R | repair', width=10, 
                                        foreground='white', background='blue')
        self.__repair_button['font'] = self.__control_font
        self.__start_button = Tk.Button(master=self.__control_label_frame, text='0 | start', width=10, 
                                        foreground='white', background='darkorchid1')
        self.__start_button['font'] = self.__control_font
        self.__stop_button = Tk.Button(master=self.__control_label_frame, text='1 | stop', width=10, 
                                        foreground='white', background='darkorchid1')
        self.__stop_button['font'] = self.__control_font
        self.__dropball_button = Tk.Button(master=self.__control_label_frame, text='2 | drop ball', width=10, 
                                        foreground='white', background='darkorchid1')
        self.__dropball_button['font'] = self.__control_font
        self.__park_button = Tk.Button(master=self.__control_label_frame, text='3 | park', width=10, 
                                        foreground='white', background='darkorchid1')
        self.__park_button['font'] = self.__control_font
        self.__reset_button = Tk.Button(master=self.__control_label_frame, text='4 | reset', width=10, 
                                        foreground='white', background='darkorchid1')
        self.__reset_button['font'] = self.__control_font
        # Dummy
        self.__sesi1_button = Tk.Button(master=self.__control_label_frame, text='sesi I', width=10, 
                                        foreground='white', background='azure4')
        self.__sesi1_button['font'] = self.__control_font
        self.__sesi2_button = Tk.Button(master=self.__control_label_frame, text='sesi II', width=10, 
                                        foreground='white', background='azure4')
        self.__sesi2_button['font'] = self.__control_font
        self.__sesi3_button = Tk.Button(master=self.__control_label_frame, text='sesi III', width=10, 
                                        foreground='white', background='azure4')
        self.__sesi3_button['font'] = self.__control_font
        self.__sesi4_button = Tk.Button(master=self.__control_label_frame, text='sesi IV', width=10, 
                                        foreground='white', background='azure4')
        self.__sesi4_button['font'] = self.__control_font
        # Position
        self.__kickoff_button.grid(row=0, column=0, padx=(5, 0))
        self.__freekick_button.grid(row=0, column=1, padx=5)
        self.__goalkick_button.grid(row=0, column=2, padx=(0, 5))
        self.__throwin_button.grid(row=1, column=0, padx=(5, 0), pady=5)
        self.__corner_button.grid(row=1, column=1, padx=5, pady=5)
        self.__penalty_button.grid(row=1, column=2, padx=(0, 5), pady=5)
        self.__start_button.grid(row=2, column=0, padx=(5, 0), pady=(0, 5))
        self.__repair_button.grid(row=2, column=1, padx=5, pady=(0, 5))
        self.__stop_button.grid(row=2, column=2, padx=(0, 5), pady=(0, 5))
        self.__dropball_button.grid(row=3, column=0, padx=(5, 0), pady=(0, 5))
        self.__park_button.grid(row=3, column=1, padx=5, pady=(0, 5))
        self.__reset_button.grid(row=3, column=2, padx=(0, 5), pady=(0, 5))
        # Dummy
        self.__sesi1_button.grid(row=4, column=0, padx=(5, 0), pady=(0, 5))
        self.__sesi2_button.grid(row=4, column=1, padx=5, pady=(0, 5))
        self.__sesi3_button.grid(row=4, column=2, padx=(0, 5), pady=(0, 5))
        self.__sesi4_button.grid(row=5, column=1, padx=5, pady=(0, 5))


    # Setter Getter   
    def set_empty_text_area(self) -> None:
        self.__text_area.delete('1.0', Tk.END)

    def set_server_ip(self, IP_ADDRESS:str) -> str:
        self.__server_ip.config(text=IP_ADDRESS)

    def set_team_name(self, team_category:str) -> str:
        self.__team_name.config(text=team_category)

    def set_team_color(self, team_color:str) -> str:
        self.__color_team_tag.config(background=team_color)




    # Testing setter
    def set_connection_status(self):
        self.__server_status.config(background='green')
    
    def set_connection_statuss(self):
        self.__server_status.config(background='red')
        