from item import Item


class Mixinlang:

    def __init__(self, *args):
        self.__language = 'EN'
        super().__init__(*args)

    @property
    def language(self):
        return self.__language

#    @language.setter
#    def language(self, value):
#        self.__language = value


    def change_lang(self):
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'


class KeyBoard(Mixinlang, Item):
    pass



