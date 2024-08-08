import tkinter as Tk
import tkinter.font as font
import customtkinter as ctk
from datetime import datetime
from tkinter import messagebox


class View:
    def __init__(self, master, controller) -> None:
        self.__controller = controller
        self.__refbox_panel(master=master)
        self.__server_panel(master=master)
        self.__prompt_panel(master=master)
        self.__robot_panel(master=master)
        # self.__control_panel(master=master)

    def __refbox_panel(self, master) -> None:
        # Frame
        self.__refbox_label_frame = ctk.CTkFrame(master=master)
        self.__refbox_label_frame.grid(row=0, column=0)
        self.__frame_title = ctk.CTkLabel(master=self.__refbox_label_frame, text='REFBOX', font=('Arial', 16, 'bold'))
        
        # Components
        self.__label_ip_refbox = ctk.CTkLabel(master=self.__refbox_label_frame, text='IP', font=('Arial', 12))
        self.__ip_refbox = ctk.CTkEntry(master=self.__refbox_label_frame, width=180)
        self.__label_port_refbox = ctk.CTkLabel(master=self.__refbox_label_frame, text='PORT', font=('Arial', 12))
        self.__port_refbox = ctk.CTkEntry(master=self.__refbox_label_frame, width=180)
        self.__connect_button = ctk.CTkButton(master=self.__refbox_label_frame, text='Connect', width=80, 
                                            fg_color='green', text_color='white', command=self.__controller.connect_refbox)
        self.__disconnect_button = ctk.CTkButton(master=self.__refbox_label_frame, text='Disconnect', width=80, 
                                               fg_color='red', text_color='white', command=self.__controller.disconnect_refbox)
        self.__connection_status = ctk.CTkFrame(master=self.__refbox_label_frame, width=35, height=25, corner_radius=5)
        self.__connection_status.configure(fg_color='red')

        # Position
        self.__frame_title.grid(row=0, column=0, columnspan=2)
        self.__label_ip_refbox.grid(row=1, column=0, padx=(10,0), sticky='w')
        self.__ip_refbox.grid(row=1, column=1, padx=10, pady=5)
        self.__label_port_refbox.grid(row=2, column=0, padx=(10,0), sticky='w')
        self.__port_refbox.grid(row=2, column=1, padx=10)
        self.__connection_status.grid(row=3, column=0, padx=(10,0), sticky='w')
        self.__connect_button.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        self.__disconnect_button.grid(row=3, column=1, padx=(105,0), sticky='w')

    def __server_panel(self, master) -> None:
        # Frame
        self.__server_label_frame = ctk.CTkFrame(master=master)
        self.__server_label_frame.grid(row=1, column=0, pady=5)
        self.__server_frame_title = ctk.CTkLabel(master=self.__server_label_frame, text='SERVER', font=('Arial', 16, 'bold'))
        
        # Components
        self.__label_ip_server = ctk.CTkLabel(master=self.__server_label_frame, text='IP', font=('Arial', 12))
        self.__server_ip = ctk.CTkLabel(master=self.__server_label_frame, text='', font=('Arial', 12))
        self.__label_port_server = ctk.CTkLabel(master=self.__server_label_frame, text='PORT', font=('Arial', 12))
        self.__port_server = ctk.CTkEntry(master=self.__server_label_frame, width=180)
        self.__connect_server_button = ctk.CTkButton(master=self.__server_label_frame, text='Connect', width=80, 
                                            fg_color='green', text_color='white', command=self.__controller.server_online)
        self.__disconnect_server_button = ctk.CTkButton(master=self.__server_label_frame, text='Disconnect', width=80, 
                                               fg_color='red', text_color='white', command=self.__controller.server_offline)
        self.__server_status = ctk.CTkFrame(master=self.__server_label_frame, width=35, height=25, corner_radius=5)
        self.__server_status.configure(fg_color='red')
        
        # Position
        self.__server_frame_title.grid(row=0, column=0, columnspan=2)
        self.__label_ip_server.grid(row=1, column=0, padx=(10,0), sticky='w')
        self.__label_port_server.grid(row=2, column=0, padx=(10,0), sticky='w')
        self.__server_ip.grid(row=1, column=1, padx=10)
        self.__port_server.grid(row=2, column=1, padx=10)
        self.__server_status.grid(row=3, column=0, padx=(10,0), sticky='w')
        self.__connect_server_button.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        self.__disconnect_server_button.grid(row=3, column=1, padx=(105,0), sticky='w')

    def __prompt_panel(self, master) -> None:
        # Frame
        self.__prompt_label_frame = ctk.CTkFrame(master=master)
        self.__prompt_label_frame.grid(row=3, column=0)
        self.__prompt_title = ctk.CTkLabel(master=self.__prompt_label_frame, text='TERMINAL', font=('Arial', 16, 'bold'))
        self.__prompt_font = ctk.CTkFont(family='Consolas', size=11, weight='bold')
        
        # Components
        self.__text_area = ctk.CTkTextbox(master=self.__prompt_label_frame, width=225, height=110, 
                                          fg_color='black', text_color='green')
        self.__text_area['font'] = self.__prompt_font
        self.__text_area.configure(state='disabled')
        self.__clear_button = ctk.CTkButton(master=self.__prompt_label_frame, text='Clear', width=80, 
                                               fg_color='blue', command=self.__controller.clear_prompt)
        
        # Position
        self.__prompt_title.grid(row=0, column=0, columnspan=2)
        self.__text_area.grid(row=1, column=0, padx=10, pady=5)
        self.__clear_button.grid(row=2, column=0, pady=(5,10))

    def __robot_panel(self, master) -> None:
        # Frame
        self.__robot_label_frame = ctk.CTkFrame(master=master)
        self.__robot_label_frame.grid(row=0, column=1, padx=(60,0), sticky='n')
        self.__robot_title = ctk.CTkLabel(master=self.__robot_label_frame, text='ROBOT INDICATOR', font=('Arial', 16, 'bold'))

        # Components
        self.__label_robot_magenta = ctk.CTkLabel(master=self.__robot_label_frame, text='MAGENTA')
        self.__magenta_status = ctk.CTkFrame(master=self.__robot_label_frame, width=35, height=25, corner_radius=5, fg_color='red')
        self.__label_robot_cyan = ctk.CTkLabel(master=self.__robot_label_frame, text='CYAN')
        self.__cyan_status = ctk.CTkFrame(master=self.__robot_label_frame,width=35, height=25, corner_radius=5, fg_color='red')
        self.__label_robot_kiper = ctk.CTkLabel(master=self.__robot_label_frame, text='KIPER')
        self.__kiper_status = ctk.CTkFrame(master=self.__robot_label_frame, width=35, height=25, corner_radius=5, fg_color='red')
        
        # Position
        self.__robot_title.grid(row=0, column=0, columnspan=3)
        self.__label_robot_magenta.grid(row=1, column=0, padx=(10,0), pady=10, sticky='w')
        self.__magenta_status.grid(row=1, column=0, padx=(80,0))
        self.__label_robot_cyan.grid(row=1, column=1, padx=(10,0), sticky='w')
        self.__cyan_status.grid(row=1, column=1, padx=(50,0))
        self.__label_robot_kiper.grid(row=1, column=2, padx=(10,0), sticky='w')
        self.__kiper_status.grid(row=1, column=2, padx=(50,10))

    def __control_panel(self, master) -> None:
        self.__control_label_frame = Tk.LabelFrame(master=master, text='CONTROL PANEL', width=200)
        self.__control_label_frame.grid(row=1, rowspan=2, column=1)
        self.__control_font = font.Font(family='Calibri', size=16, weight='bold')
        # Component
        self.__kickoff_button = Tk.Button(master=self.__control_label_frame, text='K | kick off', width=10, 
                                        foreground='white', background='blue', command=lambda: self.__controller.handle_control_button(button_id='kick off'))
        self.__kickoff_button['font'] = self.__control_font
        self.__freekick_button = Tk.Button(master=self.__control_label_frame, text='F | free kick', width=10, 
                                        foreground='white', background='blue',  command=lambda: self.__controller.handle_control_button(button_id='free kick'))
        self.__freekick_button['font'] = self.__control_font
        self.__goalkick_button = Tk.Button(master=self.__control_label_frame, text='G | goal kick', width=10, 
                                        foreground='white', background='blue',  command=lambda: self.__controller.handle_control_button(button_id='goal kick'))
        self.__goalkick_button['font'] = self.__control_font
        self.__throwin_button = Tk.Button(master=self.__control_label_frame, text='T | throw in', width=10, 
                                        foreground='white', background='blue',  command=lambda: self.__controller.handle_control_button(button_id='throw in'))
        self.__throwin_button['font'] = self.__control_font
        self.__corner_button = Tk.Button(master=self.__control_label_frame, text='C | corner', width=10, 
                                        foreground='white', background='blue',  command=lambda: self.__controller.handle_control_button(button_id='corner'))
        self.__corner_button['font'] = self.__control_font
        self.__penalty_button = Tk.Button(master=self.__control_label_frame, text='P | penalty', width=10, 
                                        foreground='white', background='blue',  command=lambda: self.__controller.handle_control_button(button_id='penalty'))
        self.__penalty_button['font'] = self.__control_font
        self.__repair_button = Tk.Button(master=self.__control_label_frame, text='R | repair', width=10, 
                                        foreground='white', background='blue',  command=lambda: self.__controller.handle_control_button(button_id='repair'))
        self.__repair_button['font'] = self.__control_font
        self.__start_button = Tk.Button(master=self.__control_label_frame, text='s | start', width=10, 
                                        foreground='white', background='darkorchid1',  command=lambda: self.__controller.handle_control_button(button_id='start'))
        self.__start_button['font'] = self.__control_font
        self.__stop_button = Tk.Button(master=self.__control_label_frame, text='S | stop', width=10, 
                                        foreground='white', background='darkorchid1',  command=lambda: self.__controller.handle_control_button(button_id='stop'))
        self.__stop_button['font'] = self.__control_font
        self.__dropball_button = Tk.Button(master=self.__control_label_frame, text='N | drop ball', width=10, 
                                        foreground='white', background='darkorchid1',  command=lambda: self.__controller.handle_control_button(button_id='drop ball'))
        self.__dropball_button['font'] = self.__control_font
        self.__park_button = Tk.Button(master=self.__control_label_frame, text='L | park', width=10, 
                                        foreground='white', background='darkorchid1',  command=lambda: self.__controller.handle_control_button(button_id='park'))
        self.__park_button['font'] = self.__control_font
        self.__reset_button = Tk.Button(master=self.__control_label_frame, text='Z | reset', width=10, 
                                        foreground='white', background='darkorchid1',  command=lambda: self.__controller.handle_control_button(button_id='reset'))
        self.__reset_button['font'] = self.__control_font
        # Dummy
        self.__sesi1_button = Tk.Button(master=self.__control_label_frame, text='1 | sesi I', width=10, 
                                        foreground='white', background='azure4', command=lambda: self.__controller.handle_control_button(button_id='sesi 1'))
        self.__sesi1_button['font'] = self.__control_font
        self.__sesi2_button = Tk.Button(master=self.__control_label_frame, text='2 | sesi II', width=10, 
                                        foreground='white', background='azure4', command=lambda: self.__controller.handle_control_button(button_id='sesi 2'))
        self.__sesi2_button['font'] = self.__control_font
        self.__sesi3_button = Tk.Button(master=self.__control_label_frame, text='3 | sesi III', width=10, 
                                        foreground='white', background='azure4', command=lambda: self.__controller.handle_control_button(button_id='sesi 3'))
        self.__sesi3_button['font'] = self.__control_font
        self.__sesi4_button = Tk.Button(master=self.__control_label_frame, text='4 | sesi IV', width=10, 
                                        foreground='white', background='azure4', command=lambda: self.__controller.handle_control_button(button_id='sesi 4'))
        self.__sesi4_button['font'] = self.__control_font
        self.__sesi5_button = Tk.Button(master=self.__control_label_frame, text='5 | sesi V', width=10, 
                                        foreground='white', background='azure4', command=lambda: self.__controller.handle_control_button(button_id='sesi 5'))
        self.__sesi5_button['font'] = self.__control_font
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
        self.__sesi4_button.grid(row=5, column=0, padx=(5, 0), pady=(0, 5))
        self.__sesi5_button.grid(row=5, column=2, padx=(0, 5), pady=(0, 5))

    # Setter   
    def set_connection_status_connected(self) -> None:
        self.__connection_status.configure(fg_color='green')
        
    def set_connection_status_disconnect(self) -> None:
        self.__connection_status.configure(fg_color='red')

    def set_prompt_log(self, message:str) -> None:
        __timestamp = datetime.now().strftime('[%H:%M:%S] ')
        self.__text_area.configure(state='normal')
        self.__text_area.insert(ctk.END, __timestamp + message + '\n')
        self.__text_area.see(ctk.END)
        self.__text_area.configure(state='disabled')
        
    def set_empty_text_area(self) -> None:
        self.__text_area.configure(state='normal')
        self.__text_area.delete('1.0', ctk.END)
        self.__text_area.configure(state='disabled')

    def set_server_ip(self, IP_server:str) -> None:
        self.__server_ip.configure(text=IP_server)

    def set_server_status_on(self) -> None:
        self.__server_status.configure(fg_color='green')
        
    def set_server_status_off(self) -> None:
        self.__server_status.configure(fg_color='red')

    def set_magenta_status_on(self) -> None:
        self.__magenta_status.configure(fg_color='green')

    def set_magenta_status_off(self) -> None:
        self.__magenta_status.configure(fg_color='red')

    def set_cyan_status_on(self) -> None:
        self.__cyan_status.configure(fg_color='green')

    def set_cyan_status_off(self) -> None:
        self.__cyan_status.configure(fg_color='red')
    
    def set_kiper_status_on(self) -> None:
        self.__kiper_status.configure(fg_color='green')

    def set_kiper_status_off(self) -> None:
        self.__kiper_status.configure(fg_color='red')

    # Getter
    def get_ip_refbox(self) -> str:
        return self.__ip_refbox.get()

    def get_port_refbox(self) -> str:
        return self.__port_refbox.get()
    
    def get_port_server(self) -> str:
        return self.__port_server.get()
    
    # Dialog
    def show_info_dialog(self, title:str, message:str) -> messagebox:
        messagebox.showinfo(title, message)

    def show_error_dialog(self, title:str, message:str) -> messagebox:
        messagebox.showerror(title, message)