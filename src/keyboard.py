from src.item import Item


class MixinLang:

    def __init__(self):
        super().__init__()
        self.language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "EN":
            self.language = "EN"
        else:
            raise AttributeError('property \'language\' of \'KeyBoard\' object has no setter')
        return self


class KeyBoard(Item, MixinLang):
    """
    Класс для представления товара “клавиатура” в магазине.
    """

    language = "EN"

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)



