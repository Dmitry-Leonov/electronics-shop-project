import csv
import os

class InstantiateCSVError(Exception):
    """Выбрасывается когда отсутствуют одно или несколько полей в файле items.csv"""
    pass

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    data_path = os.path.join(os.path.dirname(__file__), "items.csv")

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return float(self.price * self.quantity)

    def apply_discount(self) -> None:
        """ Применяет установленную скидку для конкретного товара. """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """ класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv """
        cls.all = []
        # with open('..\src\items.csv', encoding='windows-1251') as file:
        required_columns = ['name', 'price', 'quantity']
        try:
            with open(cls.data_path, encoding='windows-1251') as file:
                dict_reader_obj = csv.DictReader(file)
                for item in dict_reader_obj:
                    if not all(col in item for col in required_columns):
                        raise InstantiateCSVError("Файл items.csv поврежден")
                    cls(item['name'], float(item['price']), int(item['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(string):
        """ Статический метод, возвращающий целое число из числа - строки """
        if '.' in string:
            number = float(string)
            return int(number)
        elif string.isdigit():
            return int(string)
        else:
            raise ValueError('Невозможно преобразовать строку в число.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        """Метод сложения количества телефонов класса Item и его наследников"""
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только экземпляры Item и Phone')
        return self.quantity + other.quantity
