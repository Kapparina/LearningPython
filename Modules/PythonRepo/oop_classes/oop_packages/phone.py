from .item import Item


class Phone(Item):
    def __init__(self, *args, broken_phones: int = 0):
        super().__init__(*args)
        assert broken_phones >= 0, f"Broken Phones ({broken_phones}) is not greater than or equal to zero."

        self.broken_phones = broken_phones
