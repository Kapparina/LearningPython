import useful_tools  # Here we will import the 'useful_tools.py' module/file we created earlier.
from classes_objects import Student  # Here we have imported the 'Student' class from the 'classes_objects.py' file.

# Here we can access a function within the 'useful_tools.py' file, as well as the 'classes_objects.py' file.

print("Let's roll the dice!", useful_tools.roll_dice(10))  # This statement uses a function from 'useful_tools.py'.

student1 = Student("Jim", "Business", 3.8, False)
student2 = Student("Pam", "Art", 2.5, True)
print(student1.name)
print(student2.gpa)

print(student1.on_honour_role())