from MVC.model import Model
from MVC.view import View


class Controller:
    def __init__(self, master):
        self.__model = Model()
        self.__view = View(master=master, controller=self)