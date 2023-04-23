import pytest
from src.phone import Phone
# import csv


class TestPhone:

    def test_init(self):
        with pytest.raises(ValueError):
            Phone("iPhone 14", 120_000, 5, 0)
        phone = Phone("iPhone 14", 120_000, 5, 2)
        assert phone.number_of_sim == 2

    def test_repr(self):
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

    def test_number_of_sim(self):
        phone = Phone("iPhone 14", 120_000, 5, 2)
        with pytest.raises(ValueError):
            phone.number_of_sim = 0
        phone.number_of_sim = 1
        assert phone.number_of_sim == 1
