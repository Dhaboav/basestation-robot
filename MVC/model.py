class Model:
    def __init__(self):
        self.__refbox_dict = {
            'k':'[M] kick off', 'f':'[M] free kick', 'g':'[M] goal kick',
            't':'[M] throw in', 'c':'[M] corner', 'p':'[M] penalty',
            'K':'[C] kick off', 'F':'[C] free kick', 'G':'[C] goal kick',
            'T':'[C] throw in', 'C':'[C] corner', 'P':'[C] penalty',
            's':'start', 'S':'stop', 'N':'drop ball','L':'park', 'Z':'reset'
            }

    # Getter  
    def get_refbox_message_dict(self, key:str) -> str:
        return self.__refbox_dict.get(key, None)