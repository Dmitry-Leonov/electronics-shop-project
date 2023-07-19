import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

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
        src_path = os.path.dirname(__file__)
        src_filename = "items.csv"
        file_path = os.path.join(src_path, src_filename)
        #with open('..\src\items.csv', encoding='windows-1251') as file:
        with open(file_path, encoding='windows-1251') as file:
            DictReader_obj = csv.DictReader(file)
            for item in DictReader_obj:
                cls(item['name'], float(item['price']), int(item['quantity']))

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
