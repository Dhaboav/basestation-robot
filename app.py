import customtkinter as ctk
from MVC.controller import Controller


def main():
    root = ctk.CTk()
    root.title('Basestation Eon Teringas')

    # Popup di bagian tengah
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 640
    window_height = 480
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    root.resizable(width=False, height=False)

    Controller(master=root)
    root.mainloop()

if __name__ == "__main__":
    main()