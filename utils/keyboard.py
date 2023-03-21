from utils.item import Item


class MixinLang:
    """Класс Mixin для реализации атрибута __language и метода change_lang() для смены его значения."""

    def __init__(self, *args):
        self.__language = 'EN'
        super().__init__(*args)

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value

    @language.getter
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'


class KeyBoard(MixinLang, Item):
    """
    Класс KeyBoard, наследник классов MixinLang, Item
    """
    pass



