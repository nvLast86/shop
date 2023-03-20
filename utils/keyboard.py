from utils.item import Item


class Mixinlang:

    def __init__(self, *args):
        self.__language = 'EN'
        super().__init__(*args)

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value

    # @language.getter
    # def language(self):
    #     return self.__language


    def change_lang(self):
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'


class KeyBoard(Mixinlang, Item):
    pass



kb = KeyBoard('Dark Project KD87A', 9600, 5)
print(kb)

print(kb.language)

kb.change_lang()
print(kb.language)

kb.language = 'CH'

