from tkinter import Tk
from MVC.controller import Controller


def main():
    window = Tk()
    window.title('Basestation')
    window.geometry('660x480')
    window.resizable(width=False, height=False)
    Controller(master=window)
    window.mainloop()

if __name__ == "__main__":
    main()