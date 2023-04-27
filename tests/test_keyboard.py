"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.keyboard import KeyBoard


class TestItem:
    def test_change_lang(self):
        kb = KeyBoard('Dark Project KD87A', 9600, 5)
        kb.change_lang()
        assert kb.language == 'RU'
        kb.change_lang()
        assert kb.language == 'EN'
