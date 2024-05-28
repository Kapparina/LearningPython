from abc import ABC, abstractmethod


class Order:
    items: list = []
    quantities: list = []
    prices: list = []
    status: str = "open"
    number: int = 0

    def __init__(self, number=(number+1)):
        self.number = number

    def add_item(self, name: str, quantity: int, price: float):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_order_price(self):
        total: int = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def total_item_price(self):
        item_totals: list = []
        for i in range(len(self.prices)):
            item_totals.append(self.quantities[i] * self.prices[i])
        return item_totals

    def set_status(self, status: str):
        self.status = status

    def summary(self):
        print("---- Order summary: ----")
        print(f"Order number: {self.number:06}")
        print(f"Order status: {self.status}")
        print("\nItem name/s, quantities & prices:")
        item_details = [i for i in zip(self.items,
                                       self.prices,
                                       self.quantities,
                                       self.total_item_price())]
        print(f"{'Item Name:':<15} {'Unit Price:':^15} {'Quantity:':>15} {'Total p/item ($):':>25}")
        for item in item_details:
            print(f"{item[0]:<15} {item[1]:^15} {item[2]:>15} {item[3]:>25}")


class Authorizer(ABC):
    authorized = False

    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuth(Authorizer):

    def verify_code(self, code: int):
        print(f"Verifying code: {code}...")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class NotARobot(Authorizer):

    def not_a_robot(self):
        print("Are you a robot? Surely not...")
        self.authorized = True

    def is_authorized(self) -> bool:
        if self.authorized:
            print("Human detected!")
        else:
            print("Greetings, fellow robot!")
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code: int, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized!")
        print("Processing debit payment type...")
        print(f"Verifying security code: {self.security_code}...")
        order.set_status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code: int):
        self.security_code = security_code

    def pay(self, order: Order):
        print("Processing debit payment type...")
        print(f"Verifying security code: {self.security_code}...")
        order.status = "paid"


class PayPalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address: str, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized!")
        print("Processing PayPal payment type...")
        print(f"Verifying email address: {self.email_address}...")
        order.status = "paid"


authorizer = NotARobot()
selected_method = PayPalPaymentProcessor(email_address="bigdickswinga@money.com",
                                         authorizer=authorizer)
authorizer.not_a_robot()


order_1 = Order()
order_1.add_item(name="Keyboard",
                 quantity=1,
                 price=50)
order_1.add_item(name="SSD",
                 quantity=1,
                 price=150)
order_1.add_item(name="USB cable",
                 quantity=2,
                 price=5)

selected_method.pay(order_1)
order_1.summary()


order_2 = Order()
order_2.add_item(name="Mouse",
                 quantity=1,
                 price=20)
order_2.add_item(name="Monitor",
                 quantity=1,
                 price=200)

order_2.summary()