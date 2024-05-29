import json


class Model:
    def __init__(self):
        with open('setup.json', 'r') as json_file:
            data = json.load(json_file)

        self.__refbox_dict = {
            'k':'[M] kick off', 'f':'[M] free kick', 'g':'[M] goal kick',
            't':'[M] throw in', 'c':'[M] corner', 'p':'[M] penalty',
            'K':'[C] kick off', 'F':'[C] free kick', 'G':'[C] goal kick',
            'T':'[C] throw in', 'C':'[C] corner', 'P':'[C] penalty',
            's':'start', 'S':'stop', 'N':'drop ball','L':'park', 'Z':'reset'
        }
        
        self.__button_dict = {
            'kick off':'K', 'free kick':'F', 'goal kick':'G',
            'throw in':'T', 'corner':'C', 'penalty':'P', 'repair':'R',
            'start':'s', 'stop':'S', 'drop ball':'N', 'park':'L', 'reset':'Z',
            'sesi 1':'1', 'sesi 2':'2', 'sesi 3':'3', 'sesi 4':'4', 'sesi 5':'5'
        }

        self.__ip_address_dict = {'Cyan':data["IP_CYAN"], 'Magenta':data["IP_MAGENTA"]}
        self.__keep_character = ['s', 'S']

    # Getter  
    def get_refbox_message_dict(self, key:str) -> str:
        return self.__refbox_dict.get(key, None)
    
    def get_button_dict(self, key:str) -> str:
        return self.__button_dict.get(key, None)
    
    def get_ip_address(self) -> dict:
        return self.__ip_address_dict
    
    def get_keep_character(self, key:str) -> str:
        if key not in self.__keep_character:
            return key.upper()
        else:
            return key