import csv


class Item:
    default_discount_rate:float = 0.8
    default_markup_rate: float = 0.2
    all: list = []

    def __init__(self, name: str, price: float = 0, quantity: int = 0):
        """Validating the values of the price and quantity attributes, and assigning an object's attributes."""
        assert price >= 0, f"Price value ({price}) is not greater than zero."
        assert quantity >= 0, f"Quantity ({quantity}) is not greater than zero."

        self.__name = name  # Using the two underscores, this attribute has been made private.
        self.__price = price  # This attribute has also been made private.
        self.quantity = quantity

        Item.all.append(self)

    @property  # This is a property - a read-only attribute.
    def name(self) -> str:  # This is known as a 'getter', as it 'gets' the attribute returned within.
        """This sets the '__name' attribute to read-only, also making it accessible despite being made private."""
        return self.__name  # This tells the interpreter to refer to the '__name' attribute.

    @name.setter  # This is a 'setter' - providing a means to 'set' the value of a read-only attribute, or property.
    def name(self, value):  # This allows a user to change the value of a previously read-only attribute/property.
        """This allows setting the '__name' attribute, while also enforcing the value's type."""
        if not type(value) is str:
            raise TypeError("The 'name' attribute must be a string.")
        print(f"'{self.name}' will be named ", end="")
        self.__name = value  # This updates the value of the '__name' attribute, previously read-only.
        print(f"'{self.name}.'")

    @property
    def price(self) -> float:
        """This sets the '__price' attribute to read-only, also making it accessible despite being made private."""
        return self.__price

    def apply_default_discount(self):
        """Applies the default discount to a given item."""
        print(f"The price of '{self.name}' has been discounted from {self.price} ", end="")
        self.__price = self.__price * self.default_discount_rate
        print(f"to {self.price}.")

    def apply_discount(self, manual_discount_rate: float = 0):
        if not (manual_discount_rate > 0.0):
            return self.apply_default_discount()
        elif 0.50 <= manual_discount_rate <= 0.90:
            print(f"The price of '{self.name}' has been manually decreased from {self.price} ", end="")
            self.__price = self.__price * manual_discount_rate
            print(f"to {self.price}.")
        elif manual_discount_rate >= 0.90:
            print(f"Discounts above 90% are not permitted.")
        else:
            print(f"Discount value must range from 0.50 (50% of original) to 0.90 (90% of original).")

    def apply_default_markup(self):
        """Applies the default markup to a given item."""
        print(f"The price of '{self.name}' has been increased from {self.price} ", end="")
        self.__price = self.__price + self.__price * self.default_markup_rate
        print(f"to {self.price}.")

    def apply_markup(self, manual_markup_rate: float = 0):
        if not (manual_markup_rate > 0.0):
            return self.apply_default_markup()
        elif 0.01 <= manual_markup_rate <= 0.50:
            print(f"The price of '{self.name}' has been manually increased from {self.price} ", end="")
            self.__price = self.__price + self.__price * manual_markup_rate
            print(f"to {self.price}.")
        elif manual_markup_rate >= 0.50:
            print(f"Markups above 50% are not permitted.")
        else:
            print(f"Markup value must range from 0.01 (+1% of original) to 0.50 (+50% of original).")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open("../items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            Item(
                name=str(item.get("name")),
                price=float(item.get("quantity")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def integer_check(num) -> bool:
        """If num is a float, it will be checked against a built-in method, before being checked further."""
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def calculate_total_price(self) -> float:
        """Calculates the price when buying the total quantity of a given item."""
        return self.__price * self.quantity
