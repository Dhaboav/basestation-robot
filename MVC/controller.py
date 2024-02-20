from MVC.model import Model
from MVC.view import View


class Controller:
    def __init__(self, master):
        self.__model = Model()
        self.__view = View(master=master, controller=self)

    def clear_prompt(self):
        self.__view.set_empty_text_area()