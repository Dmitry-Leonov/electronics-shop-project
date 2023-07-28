from src.item import Item


class LanguageMixin:
    """ Класс-миксин для хранения и изменения языка клавиатуры. """

    LANGUAGES = ['EN', 'RU']

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if value not in self.LANGUAGES:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        self.__language = value

    def change_lang(self):
        """ Метод для изменения языка клавиатуры. """
        self.__language = 'RU' if self.__language == 'EN' else 'EN'
        return self


class Keyboard(Item, LanguageMixin):
    """ Класс для товара "клавиатура". """

    def __init__(self, name: str, price: float, quantity: int, language: str = 'EN') -> None:
        """
        Создание экземпляра класса Keyboard.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param language: Язык клавиатуры (по умолчанию "EN").
        """
        super().__init__(name, price, quantity)
        self.language = language
