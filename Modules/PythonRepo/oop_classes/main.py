from oop_packages import Item
from oop_packages import Phone
from oop_packages import Keyboard
from oop_packages import Email


item1 = Item("MyItem", 750)
item1.apply_markup()
item2 = Phone("MyPhone")
email1 = Email("MyEmail")
email1.send_email()
item2.apply_discount()
keyboard1 = Keyboard("HPkeyboardV12", 750.50)
keyboard1.apply_discount()
print()

print(Item.integer_check(keyboard1.price))