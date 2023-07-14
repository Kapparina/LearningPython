# Object-Oriented Programming - Student Example

class Student:  # This is a class of object known as a 'Student'.
    def __init__(self, name, age, grade):  # Upon instantiation, a 'Student' has a 'name', 'age', and 'grade'.
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):  # This method allows the retrieval of a given 'Student''s 'grade'.
        return self.grade


class Course:
    def __init__(self, name, max_students):  # Upon instantiation, a 'Course' has a 'name' and a maximum student count.
        self.name = name
        self.max_students = max_students
        self.students = []  # This is an example of an attribute belonging to a 'Course' without being a variable.

    def add_student(self, student):  # Here we add a new 'Student' to a 'Course'.
        if len(self.students) < self.max_students:  # This returns a value if 'max_students' hasn't been exceeded.
            self.students.append(student)  # This appends a 'student' to the 'students' list above.
            return True
        return False

    def get_average_grade(self):  # This is an instance method.
        value = 0
        for student in self.students:
            value += student.get_grade()  # The method is used to allow flexibility.

        return value / len(self.students)

    # A note on instance methods:

    # An 'instance method' is a method denoted by the 'self' keyword within its parentheses.
    # An instance method accesses or modifies the instance variables associated with it.


s1 = Student("John", 17, 95)  # Here we instantiate a new 'Student' class object.
s2 = Student("Jill", 19, 72)  # We instantiate another 'Student' class object.
s3 = Student("Bill", 15, 65)  # We've instantiated yet another 'Student' class object.

course = Course("Science", 2)  # We have instantiated a 'Course' class object, attributed a 'name' and 'max_students'.
course.add_student(s1)  # Now we have added a 'Student' class object to the 'student' list within the 'Course' class.
course.add_student(s2)  # As this adds the object itself to a list (despite the no. of attributes), one index is added.

# A note on how the 'students' list - an attribute of the 'Course' class - stores 's1' and 's2' in the above:

# While 's1' and 's2' are 'Student' class objects, each having multiple attributes assigned, only an object's reference
# is being appended to the 'students' list. The contents of the 'students' list would read:

#   course.students[s1, s2]

# Not:

#   course.students["John", 17, 95, "Jill", 19, 72]

# This is because the object's reference is being added to the 'students' list, and while an object has attributes,
# as per its class, the object's attributes aren't being added to the list - a reference to the object is.

# What this means is the items in the 'students' list total the number of objects added above (2: 's1' and 's2'),
# regardless of the number of attributes held by each object.

print(course.students[0].file_name)  # This prints 'name' attribute of 's1'.
print(course.add_student(s3))  # This outputs 'False' because the 'max_students' attribute would be exceeded.
print(course.get_average_grade())  # This averages the 'grade's of 's1' and 's2', as 's3' was not added to the course.


