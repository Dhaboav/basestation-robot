class Model:
    def __init__(self):
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
            'start':'0', 'stop':'1', 'drop ball':'2', 'park':'3', 'reset':'4',
            'sesi 1':'Y', 'sesi 2':'U', 'sesi 3':'V', 'sesi 4':'O'
        }

    # Getter  
    def get_refbox_message_dict(self, key:str) -> str:
        return self.__refbox_dict.get(key, None)
    
    def get_button_dict(self, key:str) -> str:
        return self.__button_dict.get(key, None)