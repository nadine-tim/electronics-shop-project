import csv
import math


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
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            print("Exception: длина наименования товара больше 10 симвовов")
            # raise ValueError("длина наименования товара больше 10 симвовов")
        self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        Item.all = []
        with open("../src/items.csv", 'r', encoding='WINDOWS-1251') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            for dct in reader:
                item = Item(dct['name'], dct['price'], dct['quantity'])

    @staticmethod
    def string_to_number(number: str):
        return math.floor(float(number))

    def __add__(self, other):
        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
