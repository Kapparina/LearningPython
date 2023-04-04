employee_file = open("../MiscFiles/employees.txt", "r")  # This will parse the file to the interpreter in 'read' mode.
# 'Read' and 'Write' modes in the context of the 'open' statement are denoted by 'r' and 'w' respectively.
print(employee_file.readable())  # The '.readable()' method tells you if the affected file is readable (via 'r' above).
for employee in employee_file.readlines():  # This will loop over each line and print it.
    print(employee)
