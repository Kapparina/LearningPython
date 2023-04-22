from oop_packages import Item
from oop_packages import Phone
from oop_packages import Keyboard
from oop_packages import Email

Item.instantiate_from_csv()

for _ in Item.all:
    print(_)

def attr_check(value):
    return value <= 50