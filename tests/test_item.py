"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
import csv


class TestItem:

    @pytest.fixture
    def item(self):
        return Item("Test Item", 10.0, 2)

    def test_repr(self):
        item1 = Item("Смартфон", 10000, 20)
        assert repr(item1) == "Item('Смартфон', 10000, 20)"

    def test_str(self):
        item1 = Item("Смартфон", 10000, 20)
        assert str(item1) == 'Смартфон'

    def test_item_initialization(self, item):
        assert item.name == "Test Item"
        assert item.price == 10.0
        assert item.quantity == 2

    def test_calculate_total_price(self, item):
        assert item.calculate_total_price() == 20.0

    def test_apply_discount(self, item):
        item.pay_rate = 0.5
        item.apply_discount()
        assert item.price == 5.0
        item.pay_rate = 1.0

    def test_name_setter(self):
        item = Item('Телефон', 10000, 5)
        item.name = 'Смартфон'
        assert item.name == 'Смартфон'
        item.name = 'СуперСмартфон'
        assert item.name == 'СуперСмартфон'

    def test_string_to_number(self):
        assert Item.string_to_number('5.0') == 5

    def test_instantiate_from_csv(cls):
        Item.all = []
        test_item = [{"name": "Смартфон", "price": "100", "quantity": "1"},
                     {"name": "Ноутбук", "price": "1000", "quantity": "3"},
                     {"name": "Кабель", "price": "10", "quantity": "5"},
                     {"name": "Мышка", "price": "50", "quantity": "5"},
                     {"name": "Клавиатура", "price": "75", "quantity": "5"}]
        with open("../src/items.csv", 'r', encoding='WINDOWS-1251') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            i = 0
            for dct in reader:
                assert test_item[i]['name'] == dct['name']
                assert test_item[i]['price'] == dct['price']
                assert test_item[i]['quantity'] == dct['quantity']
                i += 1
