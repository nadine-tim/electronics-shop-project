from src.item import Item


class MixinLang:

    layouts = ['EN', 'RU']

    def __init__(self):
        super().__init__()
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        index = self.layouts.index(self._language)
        self._language = self.layouts[1 - index]
        return self


class KeyBoard(Item, MixinLang):
    """
    Класс для представления товара “клавиатура” в магазине.
    # """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
