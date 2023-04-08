"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


class TestItem:

    @pytest.fixture
    def item(self):
        return Item("Test Item", 10.0, 2)

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
